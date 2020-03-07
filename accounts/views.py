from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignUpForm 
from django.contrib.auth.decorators import login_required
from app.models import Result,Bill

# Create your views here.


def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

        return render(request,'signup.html',{'title':'Signup','form':form})

    form = SignUpForm()
    return render(request,'signup.html',{'title':'Signup','form':form})


@login_required(login_url='login')
def myaccount(request):

    res = Result.objects.filter(user__username=request.user).order_by('-date')
    bills = Bill.objects.filter(user__username=request.user).order_by('-date')
    template_name = 'my_account.html'
    return render(request,template_name,{'title':'My Account','results':res,'bills':bills})



