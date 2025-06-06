from django.db import models

# Create your models here.
class Record(models.Model):
    sold_At = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    product_Price = models.CharField(max_length=100, blank=True, null=True)
    selling_price = models.CharField(max_length=15, blank=True, null=True)
    perchase_price = models.CharField(max_length=255, blank=True, null=True)
    quantity  = models.CharField(max_length=255, blank=True, null=True)
    warranty_period = models.CharField(max_length=255, blank=True, null=True)
    brand  = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return (f"{self.product_name}")