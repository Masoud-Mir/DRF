from django.db import models

# Create your models here.

class DigitalCurrency(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    last_price = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name