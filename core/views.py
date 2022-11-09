from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    # after posting the signup form to the databse then we get all information from the signup form:
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #    if the user already exits in the database check this:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken ❌")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken ❌")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

        else:
            messages.info(request, 'Password does not match ❌')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
