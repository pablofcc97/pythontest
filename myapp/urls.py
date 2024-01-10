from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index),
    path('',views.index, name='index'),
    path('about/',views.about,  name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/',views.tasks,  name='task'),
    path('contact/',views.contact,  name='contact')
]