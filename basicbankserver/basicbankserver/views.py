from django.shortcuts import render
from .models import accounts, customers
from django.http import HttpResponse
from django.contrib.auth import authenticate



def home(request):
    #this view will return every account
    everything = customers.objects.all()
    #creating a list to add all of the account names to (not sure if this is necessary)
    everythinglist = []
    #looping through the objects I recieve and adding the account name to my list
    for name in everything:
        everythinglist.append(name.name)
        everythinglist.append(name.email)
        everythinglist.append(name.customer_ID)

    
     
        

    #returning the list of only account names
    return HttpResponse(everythinglist)  
    



def getOne(request, name):
    #this view will return one account
    the_account = customers.objects.first()
    #this creates a list to store everything into
    list_to_send = []
    #this will add each desired property to the list
    list_to_send.append(the_account.name)

    list_to_send.append(the_account.email)

    list_to_send.append(the_account.customer_ID)

    #and returning that list
    return HttpResponse(list_to_send)



#this view will make deposits to an account
def deposit(request, account, deposit):
    #this will put the correct account in a variable
    the_account = accounts.objects.get(account_number=account)

    #this will increment the balance
    if the_account.account_balance + deposit > 100000000:
        return HttpResponse('stop being greedy')
    elif the_account.account_balance < 100000000:
        the_account.account_balance = the_account.account_balance + deposit

        the_account.save()

    #this will put the balance into a variable
    the_balance = the_account.account_balance

    #this will return the current balance
    return HttpResponse(the_balance)



#this view will delete an entire account
def delete(request, account):
    #this will delete the account requested if the account number is correct, then return it
    the_account = accounts.objects.get(account_number=account)

    if the_account.account_number == account:
        #accounts.objects.delete(account_name=name)
        the_account.delete()
    #and returning the 
    return HttpResponse(f'this is the account that was deleted {name}')




#this view will subtract from a balance
def withdraw(request, account, withdrawal):
    #this will put the correct account in a variable
    the_account = accounts.objects.get(account_name=account)

    #this will decrement the balance if my conditions are met
    if the_account.account_balance - withdrawal < 0:
        return HttpResponse('stop trying to bankrupt yourself')
    elif the_account.account_balance - withdrawal > 0:
        the_account.account_balance = the_account.account_balance - withdrawal
        the_account.save()


    #this will put the balance into a variable
    the_balance = the_account.account_balance

    #this will return the current balance
    return HttpResponse(the_balance)




#thi view will create an account
def create(request, name, email, customer_ID, account_number, account_balance, account_type):
        new_customer = customers.objects.create(name=name, email=email, customer_ID=customer_ID)
        new_customer.save()
        
        
        new_account = accounts.objects.create(account_number=account_number, account_balance=account_balance, account_type=account_type, customer_ID=new_customer)
        new_account.save()
        return HttpResponse(f'this is the newly created account number{customer_ID}, and this is the new account{new_account}')



#now we make a view for the login route
def login(request, username, password):
    #addiing the variables that will be used to authenticate
    username = username
    password = password

    User = authenticate(request, username=username, password=password)
