from django.shortcuts import render
from django.urls import path
from . import views

def return_name(request, parameter):
    return render(request, 'return_name.html', {'parameter': parameter})

urlpatterns = [
    path('<str:parameter>/', views.return_name, name='return_name'),
]

# return_name.html
<h1>The string you entered is: {{ parameter }}</h1>