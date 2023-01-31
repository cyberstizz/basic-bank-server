from django.shortcuts import render
from basicbankserver.models import accounts
from django.http import HttpResponse


def home(request):
    #this view will return every account
    everything = accounts.objects.all()
    #creating a list to add all of the account names to (not sure if this is necessary)
    everythinglist = []
    #looping through the objects I recieve and adding the account name to my list
    for name in everything:
        everythinglist.append(name.account_name)

    #returning the list of only account names
    return HttpResponse(everythinglist)  
    



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
