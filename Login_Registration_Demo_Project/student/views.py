from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def s(request):
    students = Student.objects.all()
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('s')
    return render(request,'login.html',{
        'form': form,
        'students': students,
    })