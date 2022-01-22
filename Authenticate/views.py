from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# My Classes
class AccountHandler:
    # checks if the passwords match
    def password_validate(self, pass1, pass2):
        return pass1 == pass2

    # checks if any credential already exist
    def unique_validate(self, username, email):
        username_exists = User.objects.filter(username=username)
        email_exists = User.objects.filter(email=email)
        return False if username_exists or email_exists else True

    # creating the account
    def create_account(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        user.save()
        

# Create your views here.
def home(request):
    context = {
        'title' : 'login',
    }
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            # if user exists
            login(request, user)
            messages.add_message(request, messages.INFO, 'Logged in')
            context = {'title' : 'webpage'}
            return render(request, 'Authenticate/dummy1.html', context)
        else:
            messages.add_message(request, messages.INFO, 'Bad Credentials')

    return render(request, 'Authenticate/home.html', context)


def register(request):
    context = {
        'title' : 'Register',
    }
    if request.method == 'POST':
        username = request.POST['username']
        email_address = request.POST['email-address']
        password = request.POST['password']
        password2 = request.POST['confirm-password']

        handler = AccountHandler()
        if handler.password_validate(password, password2) == True:
            if handler.unique_validate(username, email_address) == True:
                handler.create_account(username, email_address, password)
                messages.add_message(request, messages.INFO, 'Account created')
            else:
                messages.add_message(request, messages.INFO, 'Credentials exists')
        else:
            messages.add_message(request, messages.INFO, 'Password doesnt match')

    return render(request, 'Authenticate/register.html', context)


def logoff(request):
    # the name needs to be something other than logout
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out')
    return redirect('/')


@login_required
def dummypage(request):
    # the actual webpage that requires to be logged in to access
    context = {
        'title' : 'website',
    }
    return render(request, 'Authenticate/dummy1.html', context)