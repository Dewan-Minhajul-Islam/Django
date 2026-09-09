from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home_view(request):
    
    return HttpResponse("<h1>Welcome to our Home</h1>")


def student_view(re):
    
    return HttpResponse("<h1>This is students Portal</h1>")


def teacher_view(r):
    
    return HttpResponse("<h1>This is Faculty Information</h1>")

def course_view(req):
    
    return HttpResponse("<h1>Student Course</h1>")

def dept_view(req):
    
    return HttpResponse("<h1>Department Section</h1>")