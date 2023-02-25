from django.shortcuts import render
from .models import accounts
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from json import dumps, loads
from django.middleware.csrf import get_token



def home(request):

    # theUser = authenticate(request, username='tima', password='tima@tima')

    # login(request, theUser)
    #this view will return every account
    everything = User.objects.all()
    #creating a list to add all of the account names to (not sure if this is necessary)
    everythinglist = []
    #looping through the objects I recieve and adding the account name to my list
    for name in everything:
        everythinglist.append(name.username)
        everythinglist.append(name.password)

     
        
        print(f"is the user authenticated? {request.user.is_authenticated}")

    #returning the list of only account names
    return JsonResponse(everythinglist, safe=False)  

@login_required
def getOne(request):
    print(f"this is the requst.body. if you are reading this it's too late {request.user.username}")
    
    theUser = request.user
       

    theAccounts = accounts.objects.filter(user=theUser)
    #creating a data dictionary that will be sent to the client
    dataDictionary = {}

    dataDictionary.update({"data": {}})
    dataDictionary["data"].update({"username": f"{request.user}"})
    dataDictionary["data"].update({"accounts": []})
    
    for account in theAccounts:
        dataDictionary["data"]["accounts"].append({
            "accountnumber": account.account_number,
            "accounttype": account.account_type,
            "accountbalance": account.account_balance
            })
    
    return JsonResponse(dataDictionary)



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
    return HttpResponse(f'this is the account that was deleted {the_account}')




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
def thelogin(request):
    # print("HI")


    if request.method == "POST":
        data = loads(request.body)
        print(f"this is the data {data['username']}")
          
        username = data["username"]
        password = data["password"]
        this_user = authenticate(request, username=username, password=password)
        print(f"this is the user {this_user}")
        login(request, this_user)

    return HttpResponse('success')






    print(f"my authentication status is {request.user.is_authenticated}")


    print(f"my user is {request.user}")


    
#finally a view for the logout route
def the_logout(request):
    logout(request)
    return HttpResponse('all good here you are logged out!')



#this is a view for creating an account
def createAccount(request, account_number, account_balance, account_type):
        # theuser = get_user_model()

        newAccount = accounts.objects.create(account_number=account_number, account_balance=account_balance, account_type=account_type, user=theuser)


        newAccount.save()


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})



def ping(request):
    return JsonResponse({'result': 'OK'})


def csrf_failure(request, reason=""):
    ...


def testroute(request):
    theUser = authenticate(request, username='tima', password='tima@tima')
    login(request, theUser)

    theAccounts = accounts.objects.filter(user=theUser)
    #creating a data dictionary that will be sent to the client
    dataDictionary = {}

    dataDictionary.update({"data": {}})
    dataDictionary["data"].update({"username": f"{request.user}"})
    dataDictionary["data"].update({"accounts": []})
    
    for account in theAccounts:
        dataDictionary["data"]["accounts"].append({
            "accountnumber": account.account_number,
            "accounttype": account.account_type,
            "accountbalance": account.account_balance
            })
    
    return JsonResponse(dataDictionary)


    # dataDictionary.update({"user": f"{request.user}"})
    # #now turning the dictionary into json
    # dataJson = dumps(dataDictionary)
    # #and returning that list

    # print(f"my authentication status is {request.user.is_authenticated}")
    # return HttpResponse(dataJson, thisuser)

