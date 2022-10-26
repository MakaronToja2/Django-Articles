from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
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
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    return render(request, 'Accounts/logout.html', {})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {'form':form}
    return render(request, 'Accounts/register.html', context)