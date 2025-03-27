from django.contrib import admin
from Crudi.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list = ['sname','sclass']

admin.site.register(Student, StudentAdmin)