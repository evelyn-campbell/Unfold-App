from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile

# continue similarly for each page
def home(request):
    return render(request, 'core_templates/home.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'core_templates/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            # user is taken
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('signup')

            # email is taken
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('signup')
            
            # all is well, create user
            else:  
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.info(request, 'User created')

                # create user profile
                user_inst  = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_inst, account_id = user_inst.id)
                new_profile.save()
                return redirect('login')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
            
    else:
        return render(request, 'core_templates/signup.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, 'core_templates/profile.html')

@login_required(login_url='login')
def edit_profile(request):
    return render(request, 'core_templates/edit_profile.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core_templates/dashboard.html')