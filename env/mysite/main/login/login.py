from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .login_form import LoginForm



def view(request):
   	return render (request, "../templates/login/login.html")

def authenticate(request):
    # form = LoginForm(request.POST)
    # if form.is_valid():
    #         # TODO: e check dapat sa db 
    #         # if form['username'] == 'ernest' and form['password'] == '123':
    #     return render (request, "../templates/dashboard/dashboard.html")
    # else:
	    return render (request, "../templates/dashboard/dashboard.html")


