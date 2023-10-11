from niksari.models import FurnitureModel, Instruction
from rest_framework import serializers


class FurnitureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureModel
        fields = ['furniture_name', 'furniture_description',
                  'category', 'material', 'surface_finish', 'upholstery']
        
class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['instruction_text', 'material', 'surface_finish', 'upholstery']