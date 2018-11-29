from . import views
# from django.contrib import admin
from django.urls import path, re_path

app_name = 'routine'

urlpatterns = [
    # basepath
    path('', views.index, name='index'),

    # details
    re_path(r'^(?P<subject_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^teacher/$', views.information, name='information'),
]
