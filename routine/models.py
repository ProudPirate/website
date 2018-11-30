import datetime

from django.core.exceptions import ValidationError
from django.db import models
from routine.choices import teacher_title, teacher_post, day_choices


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    title = models.CharField(choices=teacher_title,max_length=5)
    post = models.CharField(choices=teacher_post,max_length=50)
    join_date = models.DateField(default=datetime.date.today)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.name


class Semester(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return 'Semester ' + str(self.number)



class Section(models.Model):
    name = models.CharField(max_length=10)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)

    class Meta:
        unique_together = [('name','department','semester')]

    def __str__(self):
        return self.name


class SectionGroup(models.Model):
    name = models.CharField(max_length=10)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,related_name='groups')

    def __str__(self):
        return '{0}/{1}'.format(self.name,self.section)


class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    is_lab = models.BooleanField(default=False)

    def __str__(self):
        return self.code + '-' + self.name


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ClassTeacherMapping(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)

    class Meta:
        unique_together =[('teacher','section')]

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.teacher.name,self.department.name,self.class_room.name)


class Period(models.Model):
    number = models.IntegerField(default=1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return 'Period {0} : {1}-{2}'.format(self.number,self.start_time,self.end_time)

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('End time cannot be greater than start time')



class Routine(models.Model):
    day = models.IntegerField(choices=day_choices)
    period = models.ForeignKey(Period,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,related_name='routines')

    def __str__(self):
        return '{0}/{1} : {2}'.format(day_choices[self.day-1][1],self.period,self.section)


class RoutineDetails(models.Model):
    routine = models.ForeignKey(Routine,on_delete=models.CASCADE,related_name='details')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    section_group = models.ForeignKey(SectionGroup, on_delete=models.CASCADE, null=True, blank=True)
    taught_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        grp_name = self.section_group.name if self.section_group is not None else 'All'
        return '{0} : {1}'.format(self.subject.code,grp_name)

    def clean(self):
        if self.subject.is_lab == False:
            details_count = self.routine.details.all().count()
            if details_count > 0:
                raise ValidationError('Class already present for given time slot.')

            if self.section_group is not None:
                raise ValidationError('Group cannot be seperated for given subject.')

        if self.subject.is_lab == True:
            details_count = self.routine.details.filter(section_group=self.section_group).count()
            if details_count > 0:
                raise ValidationError('Group already assigned for another lab class.')


#TODO : Multiple teacher for routinedetail
