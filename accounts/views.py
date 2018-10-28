from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        user = authenticate(username=usr, password=psw)

        if user and user.is_active:
            login(request, user)

    return render(request, 'accounts/login.html')