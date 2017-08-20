from django.conf.urls import url , include
from . import views
urlpatterns = [
  url('^(?P<section_code>[0-9a-zA-Z]+)/$', views.section, name='Section'),
  url('^(?P<section_code>[0-9a-zA-Z]+)/uploads/$', views.courses, name='Courses'),
  url('^(?P<section_code>[0-9a-zA-Z]+)/(?P<course_name>.+)/multi/$', views.course_view_multi, name='course_view_multi'),
  url('^(?P<section_code>[0-9a-zA-Z]+)/(?P<course_name>.+)$', views.course_view, name='course_view'),
]
