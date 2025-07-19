from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Student
from .serializers import studentserializer
from .forms import StudentForm
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

from rest_framework.generics import GenericAPIView
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
        data = request.data.copy()
        # Hash the password before saving
        if 'password' in data:
            data['password'] = make_password(data['password'])
        
        serializer = studentserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : True, 'data': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

def new_login_view(request):
    return render(request, 'new_login.html')

@api_view(['POST'])
def login_api(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({'success': False, 'message': 'Email and password required'}, status=400)
    
    try:
        student = Student.objects.get(email=email)
        if check_password(password, student.password):
            return Response({
                'success': True, 
                'message': 'Login successful',
                'student': {
                    'id': student.id,
                    'name': student.name,
                    'email': student.email
                }
            }, status=200)
        else:
            return Response({'success': False, 'message': 'Invalid password'}, status=401)
    except Student.DoesNotExist:
        return Response({'success': False, 'message': 'Student not found'}, status=404)

def dashboard_view(request):
    return render(request, 'dashboard.html')

def login_page_view(request):
    return render(request, 'login_page.html')