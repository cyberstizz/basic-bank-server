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
    the_account = accounts.objects.get(account_name=name)
    #this creates a list to store everything into
    list_to_send = []
    #this will add each desired property to the list
    list_to_send.append(the_account.account_name)

    list_to_send.append(the_account.account_balance)

    list_to_send.append(the_account.account_number)

    #and returning that list
    return HttpResponse(list_to_send)



#this view will make deposits to an account
def deposit(request, account, deposit):
    #this will put the correct account in a variable
    the_account = accounts.objects.get(account_name={account})

    #this will increment the balance
    if the_account.account_balance + deposit > 100000000:
        return HttpResponse('stop being greedy')
    elif the_account.account_balance < 100000000:
        the_account.account_balance = the_account.account_balance + deposit

    #this will put the balance into a variable
    the_balance = the_account.account_balance

    #this will return the current balance
    return HttpResponse(the_balance)



#this view will delete an entire account
def delete(request, name, account):
    #this will delete the account requested if the account number is correct, then return it
    the_account = accounts.objects.get(account_name=name)

    if the_account.account_number == account:
        accounts.objects.delete(account_name=name)
    #and returning the 
    return HttpResponse(name)




#this view will subtract from a balance
def withdraw(request, account, withdrawal):
    #this will put the correct account in a variable
    the_account = accounts.objects.get(account_name={account})

    #this will decrement the balance if my conditions are met
    if the_account.account_balance - withdrawal < 0:
        return HttpResponse('stop trying to bankrupt yourself')
    elif the_account.account_balance > 0:
        the_account.account_balance = the_account.account_balance - withdrawal


    #this will put the balance into a variable
    the_balance = the_account.account_balance

    #this will return the current balance
    return HttpResponse(the_balance)




#thi view will create an account
def create(request, accountNumber, accountBalance, accountName):
    try:
        accounts.objects.create(accounts(account_number=accountNumber, account_balance=accountBalance, account_name=accountName))
        return HttpResponse(f'this is the newly created account number{accountNumber}')
    except:
        return HttpResponse('make this make sense. that account already exists bro, or your account number ain\'t ten digits pick one.')

