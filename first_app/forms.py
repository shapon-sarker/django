from django import forms
from django.core import validators
    
class user_form(forms.Form):
    user_name = forms.CharField(label="Full_Name", widget = forms.TextInput(attrs= {'placeholder' :'Input Your Full Name'})  )
    user_phone = forms.NumberInput()
    user_email = forms.EmailField(label="User_Email",widget = forms.TextInput(attrs= {'placeholder' :'Input Your Email '})  )
    user_dob = forms.DateField(label="Date Of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    user_gender = forms.ChoiceField(choices= [('male', 'Male'), ('female', 'Female'), ('other', 'Other')], widget=forms.RadioSelect)
