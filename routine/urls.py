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
    re_path(r'^departments/$', views.departments, name='departments'),
    re_path(r'^departments/sections/(?P<sec_id>[0-9]+)/$', views.section_routine, name='section_routine'),
    re_path(r'^departments/(?P<department_id>[0-9]+)/$', views.sections, name='sections'),
]
