from django.db import models
from django.db.models import BooleanField
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=64, default='Project_name')
    link = models.URLField(default='local')
    all_users = models.ManyToManyField(User)


class ToDo(models.Model):
    is_active = BooleanField()
    note = models.CharField(max_length=64)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_user = models.OneToOneField(User, on_delete=models.CASCADE)
