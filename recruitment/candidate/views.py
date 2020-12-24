from django.shortcuts import render
from django.views.generic import CreateView
from  .models import *
# Create your views here.
class create_candidate(CreateView):
    model = Candidate
    fields =  ['company','industry','profile_name','candidate_name','location','education',
               'current_designation','current_organisation','experience','current_ctc',
               'expected_ctc','notice_period','remarks','email_id','mobile_number','cv']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def candidate_view(request,pk):
    object = Candidate.objects.filter( user = pk )
    return render(request, "candidate/candidate_view.html", {'object': object})



