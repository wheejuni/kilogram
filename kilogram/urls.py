from django.conf.urls import url
from django.urls import path

from kilogram import views

app_name = 'kilogram'

urlpatterns = [
    url(r'$', views.IndexView.as_view(), name = 'index'),
]