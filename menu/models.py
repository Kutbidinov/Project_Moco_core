from django.db import models

# Create your models here.


class Coffees(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    is_alcocol = models.BooleanField()



