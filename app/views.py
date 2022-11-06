from django.shortcuts import render , HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import sign_up
# Create your views here.

# signup view funtion 
def signup(request):
    if request.method =='POST':
        fm=sign_up(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created successfully')
    
    else:
        fm=sign_up()
    return render(request , 'signup.html' , {'form':fm})

# login view function 


def signin(request):
    if not request.user.is_authenticated:   
        if request.method=='POST':
            fm=AuthenticationForm(request=request , data=request.POST)
            if fm.is_valid():
                nm=fm.cleaned_data['username']
                ps=fm.cleaned_data['password']
                user=authenticate(username=nm , password=ps)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profileuser/')
        else:
            fm=AuthenticationForm()
        return render(request , 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profileuser/')

# profile 
def user_profile(request):
    if request.user.is_authenticated:
        return render(request , 'profile.html' , {"name":request.user})
    else:
        return HttpResponseRedirect('/loginsimply/')

# logout 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/loginsimply/')

# changepassword 
def changepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm= PasswordChangeForm(user=request.user , data=request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/profileuser/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request , 'changepass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('loginsimply')
    
# userchange form
#  view for this 

def userchangeform(request):
    
