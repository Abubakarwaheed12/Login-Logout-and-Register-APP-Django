from dataclasses import fields
import email
from pyexpat import model
from telnetlib import AUTHENTICATION


# form with django full AUTHENTICATION
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm

class sign_up(UserCreationForm):
    class Meta:
        model=User
        fields=['username' ,'first_name' , 'last_name' , 'email',]
    
    
# edit user profie form 
class editprofileform(UserChangeForm):
    password=None
    
    class Meta:
        model=User
        fields=['username' , 'first_name','last_name', 'email','date_joined','last_login']


#edit Admin Profile 
class editadminprofileform(UserChangeForm):
    password=None
    
    class Meta:
        model=User
        fields='__all__'