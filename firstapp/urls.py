from django.urls import path
from django.conf.urls import url

from firstapp import views

app_name = 'firstapp'

urlpatterns = [
  path('', views.create_topic, name='create_topic'),
  path('build', views.build_topic, name='build_topic'),
]
