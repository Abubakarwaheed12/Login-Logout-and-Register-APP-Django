from dataclasses import fields
import email
from pyexpat import model
from telnetlib import AUTHENTICATION


# form with django full AUTHENTICATION
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class sign_up(UserCreationForm):
    class Meta:
        model=User
        fields=['username' ,'first_name' , 'last_name' , 'email',]