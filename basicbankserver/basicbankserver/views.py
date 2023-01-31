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
    



def one(request, name):
    #this view will return one account
    the_account = accounts.objects.get(account_name={name})

    list_to_send = []

    list_to_send.append(the_account.account_name, the_account.account_balance, the_account.account_number)

    return HttpResponse(list_to_send)



#this view will make deposits to an account
def add(request, account, deposit):
    #this will put the correct account in a variable
    the_account = accounts.objects.get(account_name={account})

    #this will
    the_account.account_balance = the_account.account_balance + deposit

    #this will put the balance into a variable
    the_balance = the_account.account_balance

    #this will return the current balance
    return HttpResponse(the_balance)

#this view will delete an entire account
def delete(request):
    pass

#this view will subtract from a balance
def subtract(request):
    pass

#thi view will create an account
def create(request):
    pass
