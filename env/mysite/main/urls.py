from django.urls import path
from . import views
from .student import auth_login
from .login import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "main"   


urlpatterns = [
    path("", login.view, name="view"),
    
    path("authenticate/", login.authenticate, name="authenticate"),

    # Step 2  Set route name and redirect to a function
    path("dashboard", login.toDashboard, name="dashboard"),
    
    path("student-login/", auth_login.toStudentLogin, name="student-login"),
    
    path("student-register/", auth_login.toStudentRegister, name="student-register"),
    
]

urlpatterns += staticfiles_urlpatterns()