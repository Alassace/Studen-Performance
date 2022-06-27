from django.shortcuts import  render, redirect
from django.contrib import messages


def toStudentLogin(request):
   	return render (request, "../templates/student_login/student_login.html")


def toStudentRegister(request):
   return render (request, "../templates/student_register/student_register.html")