from django.conf.urls import url
from django.conf import settings
from .views import index
from django.contrib.staticfiles import views



urlpatterns = [
        url(r'^$', index),
        ]

