from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album

# Create your views here.

def index(request):
    # SELECT *FROM first_app_musician ORDER BY first_name
    Musician_list = Musician.objects.order_by('first_name')
    Album_list = Album.objects.order_by('name')
    diction = {'text_1':'This is a list of musicians', 'Musician':Musician_list, 'Album':Album_list}
    return render(request, 'first_app/index.html', context=diction)

