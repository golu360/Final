from django.shortcuts import render,redirect
from .forms import DiagnosisForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import File,Bill
from django.http import HttpResponse
import stripe

# Create your views here.
stripe.api_key = 'sk_test_suEajxhX0VNbrnS3J1RK3mMW009kdfLYqm'

def home(request):
    return render(request,'home.html',{'title':'Medica!'})





def diagnose(request):
    

    if request.method=='POST':
        form = DiagnosisForm(request.POST,request.FILES)
        print(form.is_valid())
        print(form.errors)

        if form.is_valid():
            file = File()
            image = form.cleaned_data.get('image')
            user = request.user
            file.filepath = image
            file.uploaded_user =  user
            file.save()

            
            


            
        return render(request,'diagnosis.html',{'form':form,'title':'Diagnose'})
    else:
        form = DiagnosisForm()
        return render(request,'diagnosis.html',{'form':form,'title':'Diagnose'})



    
@login_required(login_url='login')
def checkout(request):
    try:
        key = 'pk_test_PuEAnpOEYMeFF2HI8hPfiLBh00BFKBGq5R'
        template_name = 'payments.html'
        return render(request,template_name,{'title':'Checkout!','key':key})
    except stripe.error.CardError:
        return HttpResponse("Error processing card details,please retry")

    
@login_required(login_url='login')
def charge(request):
    try:
        if request.method == 'POST':
            bill = Bill.objects.create(
            user=request.user,
            amount=5.00,
            )
            charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
             )
        return render(request,'charge.html')
        
    except:
        return  redirect('diagnose')    
    
    
        