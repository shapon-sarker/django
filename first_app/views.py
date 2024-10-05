from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms 

# Create your views here.

def index(request):
    # SELECT *FROM first_app_musician ORDER BY first_name
    Musician_list = Musician.objects.order_by('first_name')
    Album_list = Album.objects.order_by('name')
    diction = {'text_1':'This is a list of musicians', 'Musician':Musician_list, 'Album':Album_list}
    return render(request, 'first_app/index.html', context=diction)

def form(request):
    new_form = forms.user_form()
    diction = {'test_form': new_form, 'heading_1': "This Form Created By Django",}

    if request.method == 'POST':
        new_form = forms.user_form(request.POST)
        if new_form.is_valid():

            user_name = new_form.cleaned_data['user_name'] # type: ignore
            user_email = new_form.cleaned_data['user_email']
            user_dob =  new_form.cleaned_data['user_dob']
            user_gender = new_form.cleaned_data['user_gender']

            diction.update({'user_name': user_name })
            diction.update({'user_email':user_email })
            diction.update({'user_dob': user_dob })
            diction.update({'user_gender': user_gender })
            diction.update({'form_submitted': "Yes" })

    return render(request, 'first_app/form.html', context=diction)

 