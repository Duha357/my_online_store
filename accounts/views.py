from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.
def login_view(request):
    success_url = reverse_lazy('products:list')

    if request.method == 'POST':
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        user = authenticate(username=usr, password=psw)

        if user and user.is_active:
            login(request, user)

        return redirect(success_url)

    return render(request, 'accounts/login.html')