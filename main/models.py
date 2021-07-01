from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=75)
    weight = models.IntegerField()
    age = models.IntegerField()
    always_hungry = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Taco(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    meat = models.BooleanField()
    spicy = models.BooleanField()
    user = models.ForeignKey(User, related_name="tacos", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
