from django.shortcuts import render
from basicbankserver.models import accounts
from django.http import HttpResponse


def home(request):
    #this view will return every account
    everything = accounts.objects.all()

    everythinglist = []

    for name in everything:
        everythinglist.append(name.account_name)


    return HttpResponse(f'<p>{everythinglist}</p>')  
    

    return all_of_them


def one(request):
    pass

#this view is to make deposits to an account
def add(request):
    pass

#this view will delete an entire account
def delete(request):
    pass

#this view will subtract from a balance
def subtract(request):
    pass

#thi view will create an account
def create(request):
    pass
