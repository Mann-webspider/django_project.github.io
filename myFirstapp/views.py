
from django.forms import EmailField
from django.shortcuts import redirect, render
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from .models import offlineFeature, onlineFeature

# Create your views here.
from django.http import HttpResponse


def index(request):
    
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        
        # print(user)
        if user is not None:
            # return render(request,'index.html')
            login(request,user)
            
            return redirect('/')
        else:
            return redirect('/signin')

    return render(request,'login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if email == User.objects.filter(email='email').exists():
                return redirect('signin')
            # return redirect(request,'signin/')
        else:
            return redirect('signin')
        user1 = User.objects.create_user(username=username, email=email, password=cpassword)
        user1.save()
        return redirect('/')
    return render(request, 'signin.html')

def online(request):
    # online = onlineFeature()  
    features = onlineFeature.objects.all()

    return render(request,'online.html',{'feature':features})

def offline(request):
    features = offlineFeature.objects.all()
    return render(request,'offline.html',{'feature': features})
def services_p(request):
    return render(request,'services.html')