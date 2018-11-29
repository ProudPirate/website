from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
from .models import Subject, Teacher
# Create your views here.


def index(request):
    all_subjects = Subject.objects.all()
    # template = loader.get_template('routine/index.html')
    context = {'all_subjects': all_subjects}
    return render(request, 'routine/index.html', context)


def detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'routine/detail.html', {'subject': subject})


def information(request):
    all_teachers = Teacher.objects.all()
    context = {'all_teachers': all_teachers}
    return render(request, 'routine/teachers.html', context)

