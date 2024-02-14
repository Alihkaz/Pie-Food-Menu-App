
#imports
from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required



def register(request):


    #if the user nfills the form after getting it , we will check the validayion of the data 
    #, then display the home page along with the sucess message
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username} , your account is created !')
            return redirect("login")
        
    #if the user request the register url , then we will give him the register form
    else:  
        form=RegisterForm()

        return render(request,'users/register.html',{'form':form})



@login_required
def profilepage(request):
    return render(request,'users/profile.html')
