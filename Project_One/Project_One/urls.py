"""
URL configuration for Project_One project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import home_view, student_view, teacher_view, course_view, dept_view
from course.views import course_info_view
from dept.views import dept_info_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('student/', student_view),
    path('teacher/', teacher_view),
    path('course/', course_view),
    path('department/', dept_view),
    path('course_info/', course_info_view),
    path('dept_info/', dept_info_view)
    
]
