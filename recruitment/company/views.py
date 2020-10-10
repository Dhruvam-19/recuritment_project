from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import companyform
from .models import Company
from . import word_document
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

def view_company(request):
    company=Company.objects.all().values()
    companylist=list(company)
    return JsonResponse({"data":companylist})

def company_view(request):
    return render(request, "company/company_view.html")

def user_company_view(request,user_id):
    from .models import Company
    object = Company.objects.filter( users = user_id ).values()
    objectlist = list(object)
    return JsonResponse({"data":objectlist})

def generate_agreement(request):
    object = Company.objects.get(id = 13)
    dict={}
    dict.__setitem__("company_name",object.company_name)
    dict.__setitem__("rate", object.fees)
    dict.__setitem__("date", object.date_of_signing)
    dict.__setitem__("payment_terms", object.payment_term)
    dict.__setitem__("validity", object.validity_of_resume)
    dict.__setitem__("replacement_period", object.replacement_period)
    object.agreement= word_document.generate_document(dict)
    object.save()
    return render(request,"company/home.html")