from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name="home"),
    path('sign_in', sign_in, name="sign_in"),
    path('sign_up', sign_up, name="sign_up"),
    path('success', success, name="success"),
    path('verify/<auth_token>', verify , name="verify"),
    path('aboutAuctionly', aboutAuctionly, name="aboutAuctionly"),
    path('contactUs', contactUs, name="contactUs"),
    path('departmentAuctionly', departmentAuctionly, name="departmentAuctionly"),
    path('liveauction', liveauction, name="liveauction"),
    path('pastauction', pastauction, name="pastauction"),
    path('upcomingauction', upcomingauction, name="upcomingauction"),
    path('emailsent', emailsent, name="emailsent")
]