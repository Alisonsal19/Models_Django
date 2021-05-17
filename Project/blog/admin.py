from django.contrib import admin
from .models import Certificate_Type, Departmnet, Faculty, Grade, Student,School
# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Departmnet)
admin.site.register(Certificate_Type)
admin.site.register(Grade)