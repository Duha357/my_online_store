from django.contrib import admin
from .models import Purchase, PurchaseItem


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem


class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'created']

    inlines = [
        PurchaseItemInline
    ]


admin.site.register(Purchase, PurchaseModelAdmin)
admin.site.register(PurchaseItem)