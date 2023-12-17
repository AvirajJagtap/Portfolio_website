# urls.py
from django.contrib import admin
from django.urls import path
from .views import about, projects, education, services, contact_view  # Update the import statement

urlpatterns = [
    path('', about, name='about'),
    path('about', about, name='about'),
    path('projects', projects, name='projects'),
    path('education', education, name='education'),
    path('services', services, name='services'),
    path('contact', contact_view, name='contact'),  # Update the function name
]
