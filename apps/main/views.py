from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def frontpage(request):
    return render(request, 'main/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('frontpage')
    else:
        form = UserCreationForm()
        
    return render(request, 'main/signup.html', {'form': form})
        
