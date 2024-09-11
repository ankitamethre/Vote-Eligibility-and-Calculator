from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'vote_valid.html')


def votecheck(request):
    try:
        age=int(request.POST['txtage'])
        if age>0 and age<18:
            result="Not eligible to vote"
        elif age>=18:
            result="Eligible to give vote"
        else:
            result="Please Give proper value"
        return render(request,'vote_valid.html',{'age':age,'res':result})
    except:
        result="please give integer value"
        return render(request,"vote_valid.html",{'res':result})