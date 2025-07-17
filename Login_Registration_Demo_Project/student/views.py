from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Student
from .serializers import studentserializer
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

@api_view(['GET','POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = studentserializer(students, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'seccess' : True, 'data': serializer.data}, status=201)
        return Response(serializer.errors, stutus=400)

def new_login_view(request):
    return render(request, 'new_login.html')