from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64),
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True, max_length=254)
