from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name