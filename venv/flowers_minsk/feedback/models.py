from django.db import models
import datetime

cur_date= datetime.datetime.now()

# Create your models here.
class Reviews(models.Model):
    CHOICES = (
        ('Дорорс','Дорорс'),
        ('Розы.бел', 'Розы.бел'),
        ('rozyminsk.by','rozyminsk.by'),
        ('daflor.by','daflor.by'),
        ('Яцветы','Яцветы')
        )
    RATE = (
        ('1','⭐'),
        ('2','⭐⭐'),
        ('3','⭐⭐⭐'),
        ('4','⭐⭐⭐⭐'),
        ('5','⭐⭐⭐⭐⭐'),
        )
    user = models.CharField(max_length=40)
    shop = models.CharField(max_length=15, choices=CHOICES)
    rating = models.CharField(max_length=1, choices=RATE)
    review = models.TextField(max_length=1000)
    date_time = models.DateField(default=f'{cur_date.year}-{cur_date.month}-{cur_date.day}')


