from django.shortcuts import render
from .models import Department, Doctor


# Create your views here.

def Home(request):
    departments = Department.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'Home.html', {"departments": departments, "doctors": doctors})

def About(request):
   
    founders = Doctor.objects.filter(pk__in=[2, 3]).order_by('pk')
    return render(request, 'About.html', {"founders": founders})

def Admin(request):
    return render(request, 'Admin.html')

def Appointments(request):
    return render(request, 'Appointments.html')

def Contacts(request):
    return render(request, 'Contacts.html')

def Services(request):
    return render(request, 'Services.html')

def Doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'Doctors.html', {"doctors": doctors})

def Departments(request):
    departments = Department.objects.all()
    return render(request, 'Departments.html', {"departments": departments})
def Forgot(request):
    return render(request, 'Forgot.html')
