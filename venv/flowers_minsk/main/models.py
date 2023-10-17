from django.db import models

class ROSES(models.Model):
    rose_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    shop = models.CharField(max_length=15)
    date_time = models.DateTimeField()
