from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name
    
class StudyField(models.Model):
   name = models.CharField(max_length=100)
   code = models.CharField(max_length=5)
   department = models.ForeignKey(Department)
	
   def __str__(self):
      return self.name
		
class Course(models.Model):
   name = models.CharField(max_length=100)
   studyfield = models.ForeignKey(StudyField)

   def __str__(self):
      return self.name
      
   def get_link_name(self):
        return self.name.replace(' ', '_')

class Section(models.Model):
   year = models.IntegerField()     
   section_number = models.IntegerField()
   studyfield = models.ForeignKey(StudyField)
   course = models.ManyToManyField(Course)
   code = models.CharField(max_length=10)
   
   def __str__(self):
      return self.code
   
class Lecturer(models.Model):
   user = models.OneToOneField(User)
   name = models.CharField(max_length=100)
   course = models.ManyToManyField(Course)
   department = models.ForeignKey(Department)
   section = models.ManyToManyField(Section)
   
   def __str__(self):
      return self.name
      

   #def name(self):
    #  return self.user.first_name + ' ' + self.user.last_name
    
def static_path(instance,filename):
   return 'main/static/'+filename
      
class Announcement(models.Model):
   pub_date = models.DateTimeField('Date Published')
   exp_date = models.DateTimeField('Expiry Date')
   message  = models.TextField()
   lecturer = models.ForeignKey(Lecturer)
   section  = models.ManyToManyField(Section)
   file1 = models.FileField(upload_to=static_path, blank=True)
   file2 = models.FileField(upload_to=static_path, blank=True)
   is_urgent = models.BooleanField(default=False)

   def __str__(self):
      return 'By: ' + self.lecturer.name
   def get_link_one(self):
      if self.file1:
        return self.file1.url.split('/')[-1]
      else:
        return ""
   def get_link_two(self):
      if self.file2:
        return self.file2.url.split('/')[-1]
      else:
        return ""
def upload_path(instance, filename):
   return 'uploads/'+instance.course.name+'/'+filename

class Material(models.Model):
   name = models.CharField(max_length=100)
   description = models.CharField(max_length=100)
   file = models.FileField(upload_to=upload_path)
   pub_date = models.DateTimeField('Date Published')   
   section = models.ManyToManyField(Section)
   lecturer  = models.ForeignKey(Lecturer)
   course = models.ForeignKey(Course)

   class Meta:
      get_latest_by = "pub_date"

   def __str__(self):
      return self.name
   def ext (self):
   	return self.file.name.split('.')[-1]
      
class Quote(models.Model):
   quote = models.CharField(max_length=140)
   author = models.CharField(max_length = 100)
   
   def __str__(self):
      return self.quote   


   
