from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def course_info_view(req):
    
    return HttpResponse("<h1>Course Informations</h1>")