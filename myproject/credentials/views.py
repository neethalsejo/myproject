from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                return redirect('register')
                messages.info(request,"Username taken")

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                print("User created")
                return render(request, "login.html")
               # return redirect('login')

        else:

            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')