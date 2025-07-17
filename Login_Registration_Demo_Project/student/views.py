from django.shortcuts import render
from .models import Student
from .forms import StudentForm
# Create your views here.
def s(request):
    # student = Student.object.all()
    # form = StudentForm()
    
    return render(request,'login.html')