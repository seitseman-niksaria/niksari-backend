from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)


class FurnitureModel(models.Model):
    name = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
