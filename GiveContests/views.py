from django.shortcuts import render
from django.http import HttpResponse
from .GetVirtualContest import MainDriver

# Create your views here.



# For Very First HomePage

def home(request):

    return render(request,'HomePage.html')


# For Listing The Contests

def virtual(request):

    user= request.GET['user']
    div= int(request.GET['div'])
    contest=MainDriver.letsGo(user,div)

    if(contest):
        return render(request, "ListPage.html",{'list':contest,'user':user,'div':div})

    else: 
        return error(request,user,div)


# For Errors while using API

def error(request,user,div):
    return render(request,'ErrorPage.html',{'user':user,'div':div})


