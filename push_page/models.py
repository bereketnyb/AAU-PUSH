from django.db import models

# Create your models here.

class ContactInfo(models.Model):
   name = models.CharField(max_length=100)
   phone = models.CharField(max_length=50)
   email = models.EmailField()
   bio = models.TextField()

   def __str__(self):
      return self.name

def upload_path(instance,filename):
   return 'Push_Page/static/'+instance.title+"-"+instance.contact.name+filename.split('.')[-1]

class PushPage(models.Model):
   title = models.CharField(max_length=150)
   content1 = models.TextField()
   content2 = models.TextField()
   img1 = models.FileField(upload_to=upload_path)
   img2 = models.FileField(upload_to=upload_path, blank=True)
   contact = models.ForeignKey(ContactInfo)
   
   def __str__(self):
      return self.title
   def get_link_one(self):
      return self.img1.url.split('/')[-1]
   def get_link_two(self):
      return self.img2.url.split('/')[-1]
