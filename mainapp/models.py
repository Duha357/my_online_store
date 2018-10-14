from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return (self.name)

class Armchair(models.Model):
    name = models.CharField(max_length=250)
    image = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT
    )
    # image = models.ImageField(
    #     upload_to='products_images',
    #     blank=True
    # )
    country = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.country:
            return (self.name, self.country)
        return (self.name)

class Table(models.Model):
    name = models.CharField(max_length=250)
    image = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT
    )
    # image = models.ImageField(
    #     upload_to='products_images',
    #     blank=True
    # )
    country = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    Manufacturer = models.ForeignKey(
        'mainapp.Manufacturer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.country:
            return (self.name, self.country)
        return (self.name)

class Lamp(models.Model):
    name = models.CharField(max_length=250)
    image = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT
    )
    # image = models.ImageField(
    #     upload_to='products_images',
    #     blank=True
    # )
    country = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    Manufacturer = models.ForeignKey(
        'mainapp.Manufacturer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.country:
            return (self.name, self.country)
        return (self.name)

class Kettle(models.Model):
    name = models.CharField(max_length=250)
    image = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT
    )
    # image = models.ImageField(
    #     upload_to='products_images',
    #     blank=True
    # )
    country = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    Manufacturer = models.ForeignKey(
        'mainapp.Manufacturer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.country:
            return (self.name, self.country)
        return (self.name)