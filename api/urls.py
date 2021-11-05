from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("listapi", views.contactlist.as_view(), name='listapi'),
]
