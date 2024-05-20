"""
URL configuration for Dgerald project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Djosiah.views import *

router = routers.DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'grades', GradeViewSet)


urlpatterns = [
    path('', include(router.urls)) # This creates a bunch of HTTP routes

    # path('admin/', admin.site.urls), # Defines end point of Django server
]

'''
GET  /students/    https://the-name-of-my-website/students/
    a list of all students

    /students/{id}
    a specific student

POST /students/   creates a new student
    
PUT /students/{id} update a specific student

DELETE /students/{id} delete a specific student
'''