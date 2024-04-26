from tabnanny import verbose

from django.db import models
from django import forms


class Cat(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class Dog(models.Model):
    name = models.CharField(max_length=10,)
    age = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
