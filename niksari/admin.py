from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(FurnitureModel)
admin.site.register(Instruction)
admin.site.register(FurnitureImage)