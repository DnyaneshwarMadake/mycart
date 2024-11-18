from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


#@login_required
def HomePage(request):
    return render (request,'index.html')



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password1')

        if pass1!=pass2:
            messages.error(request,"password not match & not same!!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,"Login Successfully")
            return redirect('login')
           

    return render(request,'signup.html')

def LoginPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('home')
            
        else:
            messages.error(request,"Username or password incorrect !!")

    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('ShopHome')
    
    
    # return render(request, 'index.html')
    # return render(request,'signup.html')