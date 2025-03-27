from django.shortcuts import render
from Crudi.models import Student

# Create your views here.
def retireview_list(request):
    student = Student.objects.all()
    return render(request, 'Crudi/templates/index.html',{'student':student})
