from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name','last_name','email','phone_number','address','state','country','accomodation','are_you_coming_alone','marital_status','age_group')