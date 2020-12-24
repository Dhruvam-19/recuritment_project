from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import companyform
from .models import Company
from . import word_document
from django.views.generic import UpdateView,DeleteView

# Create your views here.

class Update_company(UpdateView):
    model = Company
    fields = ['company_name','gst_number','ho_address','plant_address','state',
              'country','phone_number','contact_person1_name','contact_person2_name',
              'contact_person1_number','contact_person2_number','date_of_signing',
              'fees','replacement_period','payment_term','validity_of_resume',
              'remarks','type','current_status','agreement1','agreement2']
    template_name = 'company/add_company.html'

class delete_company(DeleteView):
    model = Company
    success_url = '/users/'

def home(request):
    return render(request,"users/home.html")

@login_required()
def add_new_company(request):
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

def company_view(request,user_id):
    from .models import Company
    object = Company.objects.filter( users = user_id )
    return render(request, "company/company_view.html",{'object':object})

def user_company_view(request,user_id):
    from .models import Company
    object = Company.objects.filter( users = user_id ).values()
    objectlist = list(object)
    return JsonResponse({"data":objectlist})

def generate_agreement(request,company_id):
    import pythoncom
    pythoncom.CoInitialize()
    object = Company.objects.get(id = company_id)
    dict={}
    dict.__setitem__("company_name",object.company_name.capitalize())
    dict.__setitem__("rate", object.fees)
    dict.__setitem__("date", object.date_of_signing)
    dict.__setitem__("payment_terms", object.payment_term)
    dict.__setitem__("validity", object.validity_of_resume)
    dict.__setitem__("replacement_period", object.replacement_period)
    object.agreement= word_document.generate_document(dict)
    object.save()
    return render(request,"company/home.html")

    pythoncom.CoUninitialize()