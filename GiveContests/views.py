from django.shortcuts import render
from django.http import HttpResponse
from .GetVirtualContest import MainDriver

# Create your views here.

# 1-> user not found
# 2-> no Contest Available
# 3-> Codeforces API error


# For Very First HomePage

def home(request):

    return render(request,'HomePage.html')


# For Listing The Contests

def virtual(request):

    user= request.GET['user']
    div= int(request.GET['div'])
    contest=MainDriver.letsGo(user,div)

    if(contest[0]):
        return render(request, "ListPage.html",{'list':contest[1],'user':user,'div':div})

    else:
        errNo=contest[1]
        return error(request,user,div,errNo)


# For Errors while using API

def error(request,user,div,err):

    msg={1:"Invalid Codeforces User Handle !", 2: "No Contest Available !", 3:"Codeforces Site Issue !"}

    return render(request,'ErrorPage.html',{'text':msg[err]})


