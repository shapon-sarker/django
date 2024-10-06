from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms 

# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title': 'Home Page', 'musician_list': musician_list}
    return render(request, 'first_app/index.html ', context=diction)
 
def album_list(request):
    diction = {'title': 'List OF Album'}
    return render(request, 'first_app/album_list.html ', context=diction)


def musician_form(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('musician_form')  # Use named URL pattern
        else:
            # Form is invalid, we'll render the form again with errors
            pass  # Remove the print statement
    else:
        # GET request, create a new empty form
        form = forms.MusicianForm()

    diction = {'title': 'Add Musician', 'musician_form': form}
    return render(request, 'first_app/musician_form.html', context=diction)


def album_form(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('album_form')  # Use named URL pattern
        else:
            # Form is invalid, we'll render the form again with errors
            pass  # Remove the print statement
    else:
        # GET request, create a new empty form
        form = forms.AlbumForm()

    diction = {'title': 'Add Album', 'album_form': form}
    return render(request, 'first_app/album_form.html', context=diction)