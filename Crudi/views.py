from django.shortcuts import render
from Crudi.models import Student
from Crudi.forms import StudentForms

# Create your views here.
def retireview_list(request):
    student = Student.objects.all()
    return render(request, 'Crudi/templates/index.html',{'student':student})

def Create_view(request):
    forms = StudentForms
    if request.method = 'POST'
    forms = StudentForm(request.POST)
    if form.is_valid():
        forms.save()
    return render(request,'Crudi/Create.html',{form : form})
