from django.db import models

# Create your models here.


class Subject(models.Model):
    scode = models.CharField(max_length=10)
    sname = models.CharField(max_length=50)
    sem = models.IntegerField()
    dep = models.CharField(max_length=10)

    def __str__(self):
        return self.scode + '-' + self.sname


class Teacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tid = models.CharField(max_length=10)
    tname = models.CharField(max_length=100)
    dep = models.CharField(max_length=10)

    def __str__(self):
        return self.tid + '-' + self.tname


