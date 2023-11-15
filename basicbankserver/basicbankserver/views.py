from django.shortcuts import render
from .models import accounts
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from json import dumps, loads
from django.middleware.csrf import get_token
import random




def home(request):

    # theUser = authenticate(request, username='tima', password='tima@tima')

    # login(request, theUser)
    #this view will return every account
    try:
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
    except:
        raise Http404

@login_required
def getOne(request):
    print(f"this is the requst.body. if you are reading this it's too late {request.user.username}")
    
    try:
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
    except:
        raise Http404


#this view will make deposits to an account
@login_required
def deposit(request):
    #first lets deserialize that req.body
    print('this is the withdraw view and I have been called')
    try:
        data = loads(request.body)
        print(data)


        #the informationi that I need to make the withdrawal is:
        #the account number, and the withdrawal amount

        #first lets establish the account number

        account_number = data['account_number']


        #now the withdrawal amount

        deposit_amount = data['deposit_amount']

        the_account = accounts.objects.get(account_number=account_number)

        #this will increment the balance
        if the_account.account_balance + deposit_amount > 100000000:
            return HttpResponse('stop being greedy')
        elif the_account.account_balance + deposit_amount < 100000000:
            the_account.account_balance = the_account.account_balance + deposit_amount

            the_account.save()


        #this will put the balance into a variable
        the_new_balance = the_account.account_balance

        #this will return the current balance
        return HttpResponse(f"great news! your withdrawal went through and yourt new balance is {the_new_balance}")
    except:
        raise Http404



#this view will delete an entire account
@login_required
def delete(request):

    try:
        data = loads(request.body)
        print(data)
        #this will delete the account requested if the account number is correct, then return it
        account = data['account']
        the_account = accounts.objects.get(account_number=account)

        if the_account.account_number == account:
            #accounts.objects.delete(account_name=name)
            the_account.delete()
        #and returning the 
        return HttpResponse(f'this is the account that was deleted {the_account}')
    except:
        raise Http404




#this view will subtract from a balance
@login_required
def withdraw(request):
    #first lets deserialize that req.body
    print('this is the withdraw view and I have been called')

    try:
        data = loads(request.body)
        print(data)


        #the informationi that I need to make the withdrawal is:
        #the account number, and the withdrawal amount

        #first lets establish the account number

        account_number = data['account_number']


        #now the withdrawal amount

        withdrawal_amount = data['withdrawal_amount']

        the_account = accounts.objects.get(account_number=account_number)

        #this will decrement the balance if my conditions are met
        if the_account.account_balance - withdrawal_amount < 0:
            return HttpResponse('stop trying to bankrupt yourself')
        elif the_account.account_balance - withdrawal_amount > 0:
            the_account.account_balance = the_account.account_balance - withdrawal_amount
            the_account.save()


        #this will put the balance into a variable
        the_new_balance = the_account.account_balance

        #this will return the current balance
        return HttpResponse(f"great news! your withdrawal went through and yourt new balance is {the_new_balance}")
    except:
        raise Http404



#thi view will create an account
def create(request):
        
        try:
            #first lets deserialize that req.body
            print('this is the withdraw view and I have been called')
            data = loads(request.body)
            print(data)

            print('these are the items just sent')
            print(data['username'])
            username = data['username']
            print(data['password'])
            password = data['password']
            print(data['email'])
            email = data['email']
            print(data['account'])
            account = data['account']
            print(data['deposit'])
            deposit = data['deposit']

            print(random.randint(100,999))
            account_number = random.randint(100, 999)


            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()
            
            
            new_account = accounts.objects.create(account_number=account_number, account_balance=deposit, account_type=account, user=new_user)
            new_account.save()
            return HttpResponse(f'this is the newly created account number{username}, and this is the new account{account_number}')
        except:
            raise Http404

def openCreate(request):
        try:
        #first lets deserialize that req.body
            print('this is the withdraw view and I have been called')
            data = loads(request.body)
            print(data)

            print('these are the items just sent')
            print(data['account'])
            account = data['account']
            print(data['deposit'])
            deposit = data['deposit']

            print(random.randint(100,999))
            account_number = random.randint(100, 999)


            theUser = request.user

            
            
            new_account = accounts.objects.create(account_number=account_number, account_balance=deposit, account_type=account, user=theUser)
            new_account.save()
            return HttpResponse(f'this is the newly created account number{theUser}, and this is the new account{account_number}')
        except:
            raise Http404






def delete(request):
    try:
        data = loads(request.body)
        print(data)

        print('these are the items just sent')
        print(data['delete_account'])
        account_to_delete = data['delete_account']

        theAccount = accounts.objects.get(account_number=account_to_delete)
        print(f'this is the account I have initiated to delete {theAccount}')

        theAccount.delete()
        
        return HttpResponse(f'this is the account that was deleted{theAccount}, sorry to see you go')
    except:
        raise Http404


def deleteEverything(request):
    try:
        data = loads(request.body)
        print(data)

        print(data['user'])
        user_to_delete = data['user']
        goodbye_forever = User.objects.get(username=user_to_delete)
        goodbye_forever.delete()
        
        return HttpResponse(status=200)
    except:
        raise Http404




#now we make a view for the login route
def thelogin(request):

    try:
        if request.method == "POST":
            data = loads(request.body)
            print(f"this is the username {data['username']}")
            print(f"this is the password {data['password']}")

            
            username = data["username"]
            password = data["password"]
            this_user = authenticate(request, username=username, password=password)
            print(f"this is the user {this_user}")

            if this_user is not None:
                login(request, this_user)
                return HttpResponse('success')
            else:
                return HttpResponse(status=404)
    except:
        raise Http404



    
#finally a view for the logout route
def the_logout(request):
    try:
        logout(request)
        return HttpResponse('all good here you are logged out!')
    except:
        raise Http404


#this is a view for creating an account
def createAccount(request, account_number, account_balance, account_type):
        # theuser = get_user_model()
        try:
            newAccount = accounts.objects.create(account_number=account_number, account_balance=account_balance, account_type=account_type, user=theuser)

            newAccount.save()
        except:
            raise Http404


def transfer(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            transfer_amount = data['transfer_amount']
            print(f"this is the transfer amount {transfer_amount}")
            transfer_from = data['transfer_from']
            print(f"this is the transfer from {transfer_from}")
            transfer_to = data['transfer_to']
            print(f"this is the transfer amount {transfer_to}")
            accountToTransfer = accounts.objects.get(account_number=transfer_to)
            accountFromTransfer = accounts.objects.get(account_number=transfer_from)

    #check to see if theaccount to Transfer + the transfer amount will be over 999999
    #if so return some sort of error message
        if accountToTransfer.account_balance + transfer_amount > 1000000:
            return HttpResponse(status=404)
    #check to see if the account from - the transfer amount will be under 0
    #if so, return some sort of error message
        if accountFromTransfer.account_balance - transfer_amount < 0:
            return HttpResponse(status=404)
    #subtract the transfer_amount from the transfer from account
        accountFromTransfer.account_balance = accountFromTransfer.account_balance - transfer_amount
   
    #add the transfer_amount to the transfer to account
        accountToTransfer.account_balance = accountToTransfer.account_balance + transfer_amount
    
    #save the transfer_from acccount
        accountFromTransfer.save()

    #save the transfer_to account
        accountToTransfer.save()

    #return http response with a status of 204 indicating no content, yet success
        return HttpResponse(status=204)
    


    except:
        raise Http404    


def csrf(request):
    csrf_token = get_token(request)
    print(csrf_token)

    try:
        return JsonResponse({'csrfToken': get_token(request)})
    except:
        raise Http404



def ping(request):
    try:
        return JsonResponse({'result': 'OK'})
    except:
        raise Http404



def testroute(request):
    try:
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
    except:
        raise Http404


