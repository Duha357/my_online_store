from django.db import models


class Purchase(models.Model):
    user = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        full_name = self.user.get_full_name()
        title = full_name if full_name else self.user.username
        return f'{title} {self.created.strftime("%Y-%m-%d %H-%M")}'


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
    )
    value = models.IntegerField()

    def __str__(self):
        return self.product.title