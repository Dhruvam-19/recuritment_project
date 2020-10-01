from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import companyform
# Create your views here.

def home(request):
    return render(request,"company/home.html")

@login_required()
def add_company(request):
    if request.method == 'POST':
        form = companyform(request.POST)
        form.users = request.user;
        print("methods is post ")
        if form.is_valid():
            print("form is valid")
            esave=form.save(commit=False)
            esave.users=request.user
            esave.save()

            print("Form is saved")
            return redirect("company-home")
    else:
        form = companyform()
    context = {'form' : form}

    return render(request,"company/add_company.html",context)

