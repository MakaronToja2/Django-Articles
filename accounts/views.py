from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "Accounts/login.html", context={'error':'Invalid username or password'})
        login(request, user)
        return redirect('/admin')
    return render(request, "Accounts/login.html", {})

def logout_view(request):
    return render(request, 'Accounts/login.html', {})

def register_view(request):
    return render(request, 'Accounts/login.html', {})