from django.db import models

# Create your models here.

# class Furniture(models.Model):
#     category = models.ForeignKey()

class Category(models.Model):
    category_name = models.CharField(max_length=50)

#class Type(models.Model):
#    type_name = models.CharField(max_length=50)
#    model = models.ForeignKey()
#    indoor = models.BooleanField(default=True)

class Model(models.Model):
    name = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category_id = models.ForeignKey("")
    material_id = models.ForeignKey()

class MaterialOfModel(models.Model):()

class Material(models.Model):
    name = models.CharField(max_length=50)
    material
