from django.db import models
from django.db.models.deletion import CASCADE

from django.db.models.fields import BooleanField

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    postal_code = models.IntegerField()


    def __str__(self):
        return self.school_name

class Certificate_Type(models.Model):
    certificate_name = models.CharField(max_length=250)

    def __str__(self):
        return self.certificate_name


class Grade(models.Model):
    grade = models.CharField(max_length=10)
    passing_grade = models.BooleanField(default = True)

    def __str__(self):
        return self.grade

class Faculty(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    

    def __str__(self):
        return self.last_name
    

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name



class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=CASCADE)
    Grade = models.ForeignKey(Grade, on_delete=CASCADE)
    Certificate_Type = models.ForeignKey(Certificate_Type, on_delete=CASCADE)

    def __str__(self):
        return self.full_name