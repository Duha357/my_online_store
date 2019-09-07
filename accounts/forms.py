from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm


# class SigninForm(forms.Form):
#     # Поля формы регистрации
#
#     username = forms.CharField(
#         label='Login', max_length=150,
#         widget=forms.widgets.TextInput(
#             attrs={'class': 'field_username'}
#         )
#     )
#     email = forms.CharField(
#         max_length=150, required=True,
#         widget=forms.widgets.EmailInput(
#             attrs={'class': 'field_email'}
#         )
#     )
#     password = forms.CharField(
#         max_length=250,
#         widget=forms.widgets.PasswordInput(
#             attrs={'class': 'field_password'}
#         )
#     )
#     password_confirm = forms.CharField(
#         max_length=250,
#         widget=forms.widgets.PasswordInput(
#             attrs={'class': 'field_password'}
#         )
#     )


class AccountSigninForm(forms.ModelForm):
    # Форма регистрации

    password_confirm = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        # Проверка валидности пароля

        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password is not confirm')

        return self.cleaned_data

    def save(self, commit=True):
        # Занесение данных в базу

        obj = super(AccountSigninForm, self).save(commit=False)
        password = self.cleaned_data.get('password')

        obj.set_password(password)
        obj.is_active = False

        if commit:
            obj.save()

        return obj


# class BaseSigninForm(UserCreationForm):
#     # Более высокоуровневая абстракция формы регистрации
#
#     class Meta:
#         model = Account
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def save(self, commit=True):
#         obj = super(BaseSigninForm, self).save(commit=False)
#         password = self.cleaned_data.get('password')
#
#         obj.set_password(password)
#         obj.is_active = False
#
#         if commit:
#             obj.save()
#
#         return obj