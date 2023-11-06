from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Instruction(models.Model):
    instruction_name = models.CharField(default='instruction', max_length=30)
    instruction_text = models.TextField()

    def __str__(self):
        return self.instruction_name


class FurnitureModel(models.Model):
    furniture_name = models.CharField(max_length=30)
    furniture_description = models.TextField()
    outdoor = models.BooleanField(default=False)
    leather = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructions = models.ManyToManyField(Instruction)

    def __str__(self):
        return self.furniture_name


class FurnitureImage(models.Model):
    model_image = models.ImageField()
    image_model_name = models.CharField(max_length=30)
    furniture_model = models.ForeignKey(FurnitureModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_model_name