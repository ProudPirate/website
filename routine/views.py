from django.core.serializers import json
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from routine.services import get_section_routine, get_teacher_routine
from .models import Subject, Teacher, Period, Section, RoutineDetails, Department, Semester


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
    section = get_object_or_404(Section, id=sec_id)
    routine_list = get_section_routine(section_id=sec_id)
    periods = Period.objects.all().order_by('start_time')

    routine_details = RoutineDetails.objects.filter(routine__in=section.routines.all())\
                        .order_by('subject').distinct()

    sub_teach = set(['{0} - {1}'.format(x.subject.name,
                                        x.taught_by.__str__()) for x in routine_details])

    return render(request, 'routine/section_routine.html', {'routine_list': routine_list,
                                                            'periods': periods,
                                                            'section': section,
                                                            'sub_teach': sub_teach})


def teacher_routine(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    routine_list = get_teacher_routine(taught_by__id=teacher_id)
    periods = Period.objects.all().order_by('start_time')
    print(routine_list)
    return render(request, 'routine/teacher_routine.html', {'routine_list': routine_list,
                                                            'periods': periods,
                                                            'teacher': teacher})


def departments(request):
    all_departments = Department.objects.all()
    context = {'all_departments': all_departments}
    return render(request, 'routine/department.html', context)


def departments_teachers(request):
    all_departments = Department.objects.all()
    context = {'all_departments': all_departments}
    return render(request, 'routine/department_teacher.html', context)


def sections(request, department_id):
    all_sections = Section.objects.filter(department_id=department_id)
    context = {'all_sections': all_sections}
    return render(request, 'routine/sections.html', context)


def teachers(request, department_id):
    all_teachers = Teacher.objects.filter(department_id=department_id)
    context = {'all_teachers': all_teachers}
    return render(request, 'routine/teachers.html', context)
