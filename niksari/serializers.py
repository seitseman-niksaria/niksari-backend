from niksari.models import FurnitureModel
from rest_framework import serializers


class FurnitureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureModel
        fields = ['furniture_name', 'furniture_description',
                  'category', 'material', 'surface_finish', 'upholstery']