from django.shortcuts import render
from django.http import HttpResponse

# continue similarly for each html page
def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')
