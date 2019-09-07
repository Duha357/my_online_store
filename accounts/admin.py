from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Extra', {
                'fields': ('avatar', 'age')
            },
        ),
    )

# Это вместо класса выше, не защищает контент от разных групп пользователей
# admin.site.register(Account)