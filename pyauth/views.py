from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from pyauth.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            login(request, authenticate(username=username, password=password))
            return redirect('index')
    else:
        form = UserForm()

    context = {'form': form}

    return render(request, 'pyauth/signup.html', context)