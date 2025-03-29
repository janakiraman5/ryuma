from django.shortcuts import render
from Crudi.models import Student

# Create your views here.
def retireview_list(request):
    student = Student.objects.all()
    return render(request, 'Crudi/templates/index.html',{'student':student})

def Create_view(request):
    forms = StudentForm
    return render(request,'Crudi/Create.html',{form : form})
