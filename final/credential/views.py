from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('form')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'new.html')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,
                              "Username has Taken")  # to show the messsage 'request'taken because is in def register(request)
                redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                # messages.info(request,"User Created")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return render(request, "register.html")

    return render(request, "register.html")


def form(request):
    if request.method == 'POST':
        messages.info(request,
                      "Request has send to server")  # to show the messsage 'request'taken because is in def register(request)
    return render(request, 'form.html')
