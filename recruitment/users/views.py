from django.shortcuts import render,redirect
from .forms import UserCreationForm,Userregisterform
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"users/home.html")

def register(request):
    if request.method == "POST":
        form = Userregisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            messages.success(request,f"{username} account is created")
            return redirect("login")
    else:
        form = Userregisterform()
    return render(request,"users/register.html",{"form":form})