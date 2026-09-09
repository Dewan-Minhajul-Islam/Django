from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dept_info_view(req):
    
    return HttpResponse('<h1>Department Informations</h1>')