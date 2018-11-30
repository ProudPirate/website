from django.contrib import admin
from .models import Subject, Teacher, Department, Semester, Section, SectionGroup, ClassRoom, ClassTeacherMapping, \
    Period, Routine, RoutineDetails

admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(SectionGroup)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(ClassTeacherMapping)
admin.site.register(Period)
admin.site.register(Routine)
admin.site.register(RoutineDetails)

