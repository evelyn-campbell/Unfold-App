from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile, Status

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
            # email is taken
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('signup')

            # user is taken
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
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    mystatuses = Status.objects.filter(user=request.user.username)
    return render(request, 'core_templates/profile.html', {'user_profile': user_profile, 'mystatuses': mystatuses})

@login_required(login_url='login')
def other_profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user = pk

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }

    if request.method == 'POST':
        # necessary? |
        #            V
        # friend_request = request.POST['friend_request']

        from_user = request.user
        to_user = User.objects.get(id=userID)
        friend_request, request_created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

        if request_created:

            messages.info(request, 'Friend request sent :)')
            return redirect('other_profile')
        else:

            messages.info(request, 'Friend request already sent.')
            return redirect('other_profile')

    else:
        return render(request, 'core_templates/other_profile.html', context)

@login_required(login_url='login')
def settings(request):
    if request.method == 'POST':
        new_username = request.POST['new_username']
        new_password = request.POST['new_password']
        password_confirm = request.POST['password_confirm']
        user_inst = request.user

        # change username
        if User.objects.filter(username=new_username).exists():
            messages.info(request, 'Username already exists!')
            return redirect('settings')
        elif len(new_username) > 0:
            user_inst.username = new_username
            user_inst.save()

        # change password
        if (new_password == password_confirm) and len(new_password) > 0:
            user_inst.set_password(new_password)
            user_inst.save()
            messages.info(request, 'Password updated. Please login again.')
            return redirect('login')
        elif len(new_password) > 0:
            messages.info(request, 'Passwords do not match.')
            return redirect('settings')
            
        messages.info(request, 'Profile saved.')
        return redirect('settings')
    else:
        return render(request, 'core_templates/settings.html')

@login_required(login_url='login')
def dashboard(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    statuses = Status.objects.all()
    return render(request, 'core_templates/dashboard.html', {'user_profile': user_profile, 'statuses': statuses})

@login_required(login_url='login')
def upload_status(request):
    if request.method == 'POST':
        user = request.user.username
        mood = 0 # temporary
        message = request.POST['message']
        new_status = Status.objects.create(user=user, mood=mood, message=message)
        new_status.save()
        return redirect('dashboard')
    else:
        return render(request, 'core_templates/dashboard.html')

@login_required(login_url='login')
def groups(request):
    return render(request, 'core_templates/groups.html')

@login_required(login_url='login')
def friends(request):
    return render(request, 'core_templates/friends.html')