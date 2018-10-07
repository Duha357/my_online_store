from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Manufacturer)
admin.site.register(models.Armchair)
admin.site.register(models.Table)
admin.site.register(models.Lamp)
admin.site.register(models.Kettle)