"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
# from django.contrib import admin
import login.views
import home.views
import my_profile.views
import select_schedule.views
import workout_schedule.views
import nutrient_schedule.views
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login.views.login, name='login'),
    url(r'^profile/', my_profile.views.profile, name='profile'),
    url(r'^select_schedule/', select_schedule.views.select_schedule , name='select_schedule'),
    url(r'^nutrient_schedule/', nutrient_schedule.views.nutrient_schedule, name='nutrient_schedule'),
    url(r'^workout_schedule/', workout_schedule.views.workout_schedule, name='workout_schedule'),
    url(r'^', home.views.home, name='home'),


]
