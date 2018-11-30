from . import views
# from django.contrib import admin
from django.urls import path, re_path

app_name = 'routine'

urlpatterns = [
    # basepath
    path('', views.index, name='index'),

    # details
    re_path(r'^(?P<subject_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^departments/teachers/(?P<department_id>[0-9]+)/$', views.teachers, name='teachers'),
    re_path(r'^departments/$', views.departments, name='departments'),
    re_path(r'^departments/teachers/$', views.departments_teachers, name='departments_teachers'),
    re_path(r'^departments/sections/(?P<sec_id>[0-9]+)/$', views.section_routine, name='section_routine'),
    re_path(r'^departments/teachers/r/(?P<teacher_id>[0-9]+)/$', views.teacher_routine, name='teacher_routine'),
    re_path(r'^departments/(?P<department_id>[0-9]+)/$', views.sections, name='sections'),
]
