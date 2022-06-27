from django.shortcuts import  render, redirect
from ..migrations import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
	return render (request=request, template_name="main/register/register.html")


def registerUser(request):
	if request.method == "POST":

		form = NewUserForm(request.POST)

		if form.is_valid():
			user = form.save()
            
			login(request, user)

			messages.success(request, "Registration successful." )

			return redirect("main:dashboard/dashboard.html")

		messages.error(request, "Unsuccessful registration. Invalid information.")
        
	form = NewUserForm()

	return render (request=request, template_name="main/register.html", context={"register_form":form})
    
