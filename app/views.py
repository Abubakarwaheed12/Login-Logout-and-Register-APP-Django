from django.shortcuts import render , HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import sign_up , editprofileform , editadminprofileform
from django.contrib.auth.models import User , Group
# Create your views here.

# signup view funtion 
def signup(request):
    if request.method =='POST':
        fm=sign_up(request.POST)
        if fm.is_valid():
            fm.save()
            # group=Group.objects.get(name='editor')
            # user.Groups.add(group)
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
        if request.method=='POST':
            if request.user.is_superuser==True:
                fm=editadminprofileform(request.POST, instance=request.user)
                users=User.objects.all()
            else:
                users=None
                fm=editprofileform(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request , "Profile upodated succesfully")
        else:
            if request.user.is_superuser==True:
                users=User.objects.all()
                fm=editadminprofileform(instance=request.user)
            else:
                users=None
                fm=editprofileform(instance=request.user)
        return render(request , 'profile.html' , {"name":request.user , "form":fm , 'users':users})
    else:
        return HttpResponseRedirect('/loginsimply/')

# logout 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

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
    
# specific user details 

def userdetails(request , id):
    if User.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=editadminprofileform(instance=pi)
        return render(request, 'userdetails.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/loginsimply/')
        

   
