from django.conf.urls import url , include
from . import views

urlpatterns = [
    url('^(?P<quick_page>[0-9]+)/$',views.Push_Page, name='Quick_Page'),
    ]
