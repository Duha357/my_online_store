from django.urls import path
from accounts.views import login_view, account_signin

app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('signin/', account_signin, name='signin'),
]