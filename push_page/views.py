from django.shortcuts import render
from .models import *

# Create your views here.

def Push_Page(request,quick_page):
    archives = PushPage.objects.all()
    page = PushPage.objects.get(id=quick_page)
    context = {'page':page,'archives':archives}
    return render(request,'push_page/Push_Page.html',context)
