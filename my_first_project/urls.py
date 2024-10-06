from django.contrib import admin
from django.urls import path
from first_app import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('album_list/', views.album_list, name='album_list'),   
    path('album_form/', views.album_form, name='album_form'),
    path('musician_form/', views.musician_form, name='musician_form'),
]
