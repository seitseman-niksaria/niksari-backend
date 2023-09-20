from django.db import models

# Create your models here.

class Furniture(models.Model):
    category = models.ForeignKey()

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    type = category = models.ForeignKey()

class Type(models.Model):
    type_name = models.CharField(max_length=50)
    model = models.ForeignKey()
    indoor = models.BooleanField(default=True)

class Model(models.Model):
    name = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
