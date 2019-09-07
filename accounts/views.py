from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from accounts.forms import AccountSigninForm
from django.core.mail import send_mail


def login_view(request):
    # Логика авторизации

    success_url = reverse_lazy('products:product_list')

    if request.method == 'POST':
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        user = authenticate(username=usr, password=psw)

        if user and user.is_active:
            login(request, user)

        return redirect(success_url)

    return render(request, 'accounts/login.html')


# def account_signin(request):
#     success_url = reverse_lazy('products:product_list')
#     form = AccountSigninForm()
#
#     if request.method == 'POST':
#         form = AccountSigninForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             send_mail(
#                 'Signin User',
#                 'Test Message',
#                 from_email='info@project.ru',
#                 recipient_list=[email]
#             )
#             form.save()
#         return redirect(success_url)
#
#     return render(request, 'accounts/signin.html', {'form': form})


def account_signin(request):
    # Отправка письма, подтверждение роегистрации

    success_url = reverse_lazy('products:product_list')
    form = AccountSigninForm()

    if request.method == 'POST':
        form = AccountSigninForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            send_mail(
                'Signin User',
                'Test Message',
                from_email='info@project.ru',
                recipient_list=[user.email]
            )
        return redirect(success_url)

    return render(request, 'accounts/signin.html', {'form': form})


# @login_required(login_url=reverse_lazy('accounts:login')
# def confirm_account(request):
#     success_url = reverse_lazy('products:product_list')
#
#     request.user.is_active = True
#
#     return redirect(success_url)