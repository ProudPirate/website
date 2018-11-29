from . import views
from django.urls import path, re_path

app_name = 'dashboard'

urlpatterns = [
    # basepath
    path('', views.home, name='home'),

    # details
    # re_path(r'^(?P<subject_id>[0-9]+)/$', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup')
]