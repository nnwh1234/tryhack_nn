from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, NewEntry
from .models import Entry

# Create your views here.
@login_required
def index(response):
    if response.method == 'POST':
        new_entry = NewEntry(response.POST)
        if new_entry.is_valid():
            new_entry_saved = new_entry.save(commit=False)
            new_entry_saved.user = response.user
            new_entry_saved.save()
            return redirect('index')
    else:
        new_entry = NewEntry()
    return render(response, 'index.html', {'form': new_entry})

@login_required
def entries(response):
    user_entries = Entry.objects.filter(user=response.user).order_by('-date')
    return render(response, 'entries.html', {'entries':user_entries})


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form": form})
