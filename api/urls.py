from django.conf.urls import url

from . import views

# Url patterns
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^study_fields', views.study_fields, name='study_fields'),
	url(r'^courses', views.courses, name="courses"),
	url(r'^announcements', views.announcements, name="announcements"),
	url(r'^materials', views.materials, name="materials"),
	url(r'^section_exists', views.section_exists, name="section_exists"),
	url(r'^sections', views.sections, name="sections"),
]
