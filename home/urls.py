from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),
    path("profile", views.profile,name='profile'),
    path("result", views.result,name='result'),
]

urlpatterns += staticfiles_urlpatterns()