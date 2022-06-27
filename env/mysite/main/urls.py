from django.urls import path
from . import views
from .login import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "main"   


urlpatterns = [
    path("", login.view, name="view"),
    
    path("authenticate/", login.authenticate, name="authenticate"),

    # Ma add sang routes sang dashboard

    
    path("register", views.register_request, name="register")

    path("dashboard", views.register_request, name="dashboard")
         
]

urlpatterns += staticfiles_urlpatterns()