from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company_name = models.CharField(max_length=128)
    description = models.TextField()
    CATEGORY = (
        ('1', ('Men wear')),
        ('2', ('Women wear')),
        ('3', ('Bags')),
        ('4', ('Watches')),
        ('5', ('Kids')),

    )
    category = models.CharField(max_length=128, choices=CATEGORY)
    picture = models.ImageField(upload_to="productImages", null=True, blank=True)
