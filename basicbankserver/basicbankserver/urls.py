"""basicbankserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('accounts', views.getOne, name='home'),
    path('accounts/login/', include("django.contrib.auth.urls")),
    path('accounts/login/', views.thelogin, name='accountslogin'),
    path('deposit', views.deposit, name='deposit'),
    path('accounts/delete/<int:account>', views.delete, name='delete'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('create/<int:accountNumber>/<int:accountBalance>/<str:accountName>/', views.create, name='create'),
    path('login', include('django.contrib.auth.urls')),
    path('login', views.thelogin, name='login'),
    path('logout', views.the_logout, name='logout'),
    path('create_account/<int:account_number>/<int:account_balance>/<str:account_type>', views.createAccount, name='create_account'),
    path('csrf/', views.csrf, name='csrf'),
    path('ping/', views.ping, name='ping'),
    path('testroute/', views.testroute, name='testroute'),

]



"""
 this is the codecademy code below
 
from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404

def home(request):
  try:
    found_pet = Patient.objects.get(pk=1)
  except Patient.DoesNotExist:
    raise Http404()
  context = {"name": "Djangoer", "pet": found_pet}
  return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
  model = Owner
  template_name = "vetoffice/owner_list.html"

class PatientList(ListView):
  model = Patient
  template_name = "vetoffice/patient_list.html"

class OwnerCreate(CreateView):
  model = Owner
  template_name = "vetoffice/owner_create_form.html"
  fields = ["first_name", "last_name", "phone"]

class PatientCreate(CreateView):
  model = Patient
  template_name = "vetoffice/patient_create_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class OwnerUpdate(UpdateView):
  model = Owner
  template_name = "vetoffice/owner_update_form.html"
  fields = ["first_name", "last_name", "phone"]
  success_url = "/vetoffice/owner/list"

class PatientUpdate(UpdateView):
  model = Patient
  template_name = "vetoffice/patient_update_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]
  success_url = "/vetoffice/patient/list"

class OwnerDelete(DeleteView):
  model = Owner
  template_name = "vetoffice/owner_delete_form.html"
  success_url = "/vetoffice/owner/list"

class PatientDelete(DeleteView):
  model = Patient
  template_name = "vetoffice/patient_delete_form.html"
  success_url = "/vetoffice/patient/list" 
"""
