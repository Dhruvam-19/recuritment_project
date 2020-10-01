from django import forms
from .models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row,Column,Submit

class companyform(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('company_name', css_class='form-group col-md-4 mb-0'),
                Column('gst_number', css_class='form-group col-md-4 mb-0'),
                Column('type', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'),
            Row(Column('ho_address', css_class='form-group col-md-3 mb-0'),
                Column('plant_address', css_class='form-group col-md-3 mb-0'),
                Column('state', css_class='form-group col-md-3 mb-0'),
                Column('country',css_class='form-group col-md-3 mb-0'),
                css_class='form-row'),
            Row(Column('contact_person1_name', css_class='form-group col-md-6 mb-0'),
                Column('contact_person1_number', css_class='form-group col-md-6 mb-0'),
                Column('contact_person2_name', css_class='form-group col-md-6 mb-0'),
                Column('contact_person2_number', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'),
            Row(Column('contact_person1_name', css_class='form-group col-md-6 mb-0'),
                Column('contact_person1_number', css_class='form-group col-md-6 mb-0'),
                Column('contact_person2_name', css_class='form-group col-md-6 mb-0'),
                Column('contact_person2_number', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'),
            Row(Column('date_of_signing', css_class='form-group col-md-4 mb-0'),
                Column('fees', css_class='form-group col-md-4 mb-0'),
                Column('replacement_period', css_class='form-group col-md-4 mb-0'),
                Column('payment_term', css_class='form-group col-md-6 mb-0'),
                Column('validity_of_resume', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            Row(Column('remarks', css_class='form-group col-md-6 mb-0'),
                Column('current_status', css_class='form-group col-md-6 mb-0'),
                Column('agreement1', css_class='form-group col-md-6 mb-0'),
                Column('agreement2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            Submit('submit', 'Save Details')

        )

    class Meta:
        model = Company
        fields=['company_name','gst_number','type','ho_address','plant_address','state','country',
                'contact_person1_name','contact_person1_number','contact_person2_name',
                'contact_person2_number','phone_number','date_of_signing','fees',
                'replacement_period','payment_term','validity_of_resume','remarks',
                'current_status','agreement1','agreement2']

