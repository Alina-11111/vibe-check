from django.shortcuts import render, redirect
#from django.contrib.auth.forms import PersonForm
from .forms import PersonForm

def home(request):
    return render (request, 'moodspace/home.html')

def registration(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PersonForm()
    
    return render(request, 'moodspace/register.html', {'form': form})

