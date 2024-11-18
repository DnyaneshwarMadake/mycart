from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib auth.forms import UserCreationForm
from accounts.forms import UserForm

def register(request):
    if request.method=="POST":
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=email,password=password)
            login(request,user)
            return redirect('shop')
    else:
        form =UserForm()
    return render(request,'registration/registration.html',{'form':form})


