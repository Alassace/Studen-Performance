from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .login_form import LoginForm



def view(request):
   	return render (request, "../templates/login/login.html")

def authenticate(request):
  return render (request, "../templates/dashboard/dashboard.html")

# Step 3 create a function that points to an html 
def toDashboard(request):
    isUserNameTrue = request.POST['email'] == 'ernest'
    
    isPasswordTrue = request.POST['password'] == '123'
    
    if isUserNameTrue and isPasswordTrue:
        return render (request,'../templates/dashboard/dashboard.html')
    else:
   	    return render (request, "../templates/login/login.html")
