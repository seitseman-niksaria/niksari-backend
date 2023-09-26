from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name


class Upholstery(models.Model):
    upholstery_name = models.CharField(max_length=50)
    def __str__(self):
        return self.upholstery_name


class Material(models.Model):
    material_name = models.CharField(max_length=50)
    def __str__(self):
        return self.material_name


class SurfaceFinish(models.Model):
    surface_finish_name = models.CharField(max_length=50)
    def __str__(self):
        return self.surface_finish_name


class FurnitureModel(models.Model):
    furniture_name = models.CharField(max_length=50)
    furniture_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    surface_finish = models.ForeignKey(SurfaceFinish, on_delete=models.CASCADE)
    upholstery = models.ForeignKey(Upholstery, on_delete=models.CASCADE, default="No upholstery")
    def __str__(self):
        return self.furniture_name


class Instruction(models.Model):
    instruction_text = models.TextField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    surface_finish = models.ForeignKey(SurfaceFinish, on_delete=models.CASCADE)
    upholstery = models.ForeignKey(Upholstery, on_delete=models.CASCADE)
    def __str__(self):
        return self.instruction_id
