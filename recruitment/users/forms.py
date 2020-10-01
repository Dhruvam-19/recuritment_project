from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row,Column,Submit

class DateInput(forms.DateInput):
    input_type = 'date'

class Userregisterform(UserCreationForm):
    email =forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class profile_form(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput(attrs={'placholder':'Birth Date'}),required=False)
    joining_date = forms.DateField(widget=DateInput(attrs={'placholder': 'Joining Date'}),required=False)
    resignation_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'Resignaiton date'}),required=False)
    image = forms.ImageField (required=False)
    document1 = forms.ImageField (required=False)
    document2 = forms.ImageField (required=False)
    document3 = forms.ImageField (required=False)
    agreement_document = forms.ImageField (required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'image',
            Row(Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('middle_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'),
            Row(Column('father_first_name',css_class='form-group col-md-4 mb-0'),
                Column('father_middle_name',css_class='form-group col-md-4 mb-0'),
                Column('father_last_name',css_class='form-group col-md-4 mb-0'),
                Column('date_of_birth',css_class='form-group col-md-4 mb-0'),
                Column('joining_date',css_class='form-group col-md-4 mb-0'),
                Column('resignation_date',css_class='form-group col-md-4 mb-0'),
                Column('adharcard_number',css_class='form-group col-md-4 mb-0'),
                Column('pan_number',css_class='form-group col-md-4 mb-0'),
                css_class='form-row'),
            Row(Column('email',css_class='form-group col-md-4 mb-0'),
                Column('phone_number1',css_class='form-group col-md-4 mb-0'),
                Column('phone_number2',css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
                ),
            'address_lane1',
            'address_lane2',
            'address_lane3',
            Row(Column('country', css_class='form-group col-md-4 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'),
            Row(Column('bank_name',css_class='form-group col-md-4 mb-0'),
                Column('bank_branch',css_class='form-group col-md-4 mb-0'),
                Column('account_number',css_class='form-group col-md-4 mb-0'),
                Column('micr_code',css_class='form-group col-md-4 mb-0'),
                Column('ifsc_code',css_class='form-group col-md-4 mb-0'),
                css_class='form-row'),
            Row(Column('bd',css_class='form-group col-md-4 mb-0'),
                Column('execution',css_class='form-group col-md-4 mb-0'),
                css_class='form-row'),
            Row(Column('agreement_document',css_class='form-group col-md-4 mb-0'),
                Column('document1',css_class='form-group col-md-6 mb-0'),
                Column('document2',css_class='form-group col-md-6 mb-0'),
                Column('document3',css_class='form-group col-md-46 mb-0'),
                css_class='form-row'),
            Submit('submit', 'Save Details'))

    class Meta:
         model = profile
         fields = ['image','first_name','middle_name','last_name',
                   'father_first_name','father_middle_name',
                   'father_last_name','address_lane1','address_lane2',
                   'state','ifsc_code','email','phone_number1','phone_number2',
                   'address_lane3','country','bank_name','bank_branch','date_of_birth',
                   'joining_date','resignation_date',
                   'pan_number','account_number','micr_code','adharcard_number',
                   'execution','bd','agreement_document','document1',
                   'document2','document3']

