from django.core.serializers import json
from django.shortcuts import render, get_object_or_404

from routine.services import get_section_routine
from .models import Subject, Teacher, Period


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


def section_routine(request, sec_id):
    routine_list = get_section_routine(sec_id)
    periods = Period.objects.all().order_by('start_time')
    print(routine_list)
    return render(request, 'routine/section_routine.html', {'routine_list': routine_list,'periods':periods})
