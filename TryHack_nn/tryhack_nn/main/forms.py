from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", 'password1', 'password2']
    
class NewEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'mood', 'content']
        labels = {
            'title': 'What happened? (title)',
            'mood': 'How are you feeling?',
            'content': 'Tell me more about it... (description)'
        }
