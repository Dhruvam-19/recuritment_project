from django.shortcuts import render,redirect
from .forms import UserCreationForm,Userregisterform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import profile_form

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

@login_required()
def profile(request):
    if request.method == 'POST':
        form = profile_form(request.POST,request.FILES,instance=request.user.profile)
        print("inside post ")
        if form.is_valid():
            print("Inside valid condition")
            form.save()
            return redirect("home")
    else:
        form = profile_form(instance=request.user.profile)

    return render(request, "users/demo_profile.html", {
        "form": form
    })