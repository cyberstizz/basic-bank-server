from django.shortcuts import render


def home(request):
    #this view will return every account
    return render('hello stizz')


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