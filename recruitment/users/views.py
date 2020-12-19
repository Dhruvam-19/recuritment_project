from django.shortcuts import render,redirect
from .forms import UserCreationForm,Userregisterform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import profile_form
from django.views.generic import UpdateView
from .models import profile

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
def create_profile(request):
    if request.method == 'POST':
        form = profile_form(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = profile_form(instance=request.user.profile)

    return render(request, "users/demo_profile.html", {
        "form": form
    })

@login_required()
def profile_view(request,profile_id):
    from .models import profile
    object = profile.objects.filter( pk = profile_id).first()
    return render(request,"users/profile_view.html",{'object':object})


def index(request):
    return render(request,"index.html")

def auth_register(request):
    return render(request,"auth-register.html")

class ProfileUpdateView(UpdateView):
    model = profile
    fields = [ 'image','first_name','middle_name','last_name',
               'father_first_name','father_middle_name','father_last_name',
               'date_of_birth','joining_date','resignation_date','email',
               'phone_number1','phone_number2','address_lane1','address_lane1','address_lane2',
               'address_lane3','state','country','bank_name','bank_branch','pan_number',
               'account_number','ifsc_code','micr_code','adharcard_number','document1','document2',
               'document3','execution','bd','agreement_document']
    template_name = "users/profile.html"