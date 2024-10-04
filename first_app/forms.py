from django import forms
    
class user_form(forms.Form):
    user_name = forms.CharField(label="Full_Name", widget = forms.TextInput(attrs= {'placeholder' :'Input Your Full Name'})  )
    user_phone = forms.NumberInput()
    user_email = forms.EmailField(label="User_Email",widget = forms.TextInput(attrs= {'placeholder' :'Input Your Email '})  )
    user_phone = forms.NumberInput()
