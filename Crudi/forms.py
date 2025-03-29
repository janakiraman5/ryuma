from django import forms
from Crudi.models import Student

class StudentForms(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'
    
