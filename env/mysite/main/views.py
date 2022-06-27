from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
    return render (request,template_name='main/templates/dashboard/dashboard.html')


def homepage(request):
    return render (request=request, template_name="main/home.html")


