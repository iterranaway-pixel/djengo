from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('mynotes/',views.notess,name='mynotes'),
    path('about/',views.about,name='about')
]