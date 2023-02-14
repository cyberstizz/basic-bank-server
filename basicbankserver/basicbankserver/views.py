from django.shortcuts import render
from .models import accounts, customers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def home(request):
    #this view will return every account
    everything = customers.objects.all()
    #creating a list to add all of the account names to (not sure if this is necessary)
    everythinglist = []
    #looping through the objects I recieve and adding the account name to my list
    for name in everything:
        everythinglist.append(name.username)
        everythinglist.append(name.password)

    
     
        

    #returning the list of only account names
    return JsonResponse(everythinglist)  
    


def getOne(request):
    #this view will return one account
    theusername = customers.objects.get(username="meatball")

    theAccounts = accounts.objects.filter(user=theusername)

    #creating a data dictionary that will be sent to the client
    dataDictionary = {}


    for account in theAccounts:
        accountdict = {}
        accountdict.update({"accountnumber": account.account_number})
        accountdict.update({"accounttype": account.account_type})
        dataDictionary.update({f"{account}Object": accountdict})
    # auser = the_account.password
    #this creates a list to store everything into
    # dictionary_to_send = {}
    #this will add each desired property to the list
    # dictionary_to_send.update({"account": the_account})

    #this will grab all accounts associated with this particular user
    # all_users_accounts = accounts.objects.all(user=the_account)

    # dictionary_to_send.accounts = all_users_accounts

    #and returning that list
    return HttpResponse(dataDictionary)



#this view will make deposits to an account
@login_required
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
@login_required
def delete(request, account):
    #this will delete the account requested if the account number is correct, then return it
    the_account = accounts.objects.get(account_number=account)

    if the_account.account_number == account:
        #accounts.objects.delete(account_name=name)
        the_account.delete()
    #and returning the 
    return HttpResponse(f'this is the account that was deleted {name}')




#this view will subtract from a balance
@login_required
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
def create(request, username, password, account_number, account_balance, account_type):
        new_user = User.objects.create(username=username, password=password)
        new_user.save()
        
        
        new_account = accounts.objects.create(account_number=account_number, account_balance=account_balance, account_type=account_type, user=new_user)
        new_account.save()
        return HttpResponse(f'this is the newly created account number{username}, and this is the new account{new_account}')



#now we make a view for the login route
def login(request, username, password):
    #addiing the variables that will be used to authenticate
    username = username
    password = password

    User = authenticate(request, username=username, password=password)

    login(request, User)


#finally a view for the logout route
def logout(request):
    logout(request)



#this is a view for creating an account
def createAccount(request, account_number, account_balance, account_type):
        theuser = get_user_model()

        newAccount = accounts.objects.create(account_number=account_number, account_balance=account_balance, account_type=account_type, user=theuser)


        newAccount.save()