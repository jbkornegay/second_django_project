from django.contrib import admin
from .models import School, Student, Certificate_Type, Grade, Faculty, Department

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Certificate_Type)
admin.site.register(Grade)
admin.site.register(Faculty)
admin.site.register(Department)

