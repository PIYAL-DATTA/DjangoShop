from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.homefunc, name='homefunc'),
    path('order/', views.formvalue, name='formvalue'),
]