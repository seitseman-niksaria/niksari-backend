from niksari.models import FurnitureModel, Instruction
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField



class FurnitureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureModel
        fields = ['id', 'furniture_name', 'furniture_description','outdoor','leather',
                  'category', 'instructions']
        
class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id', 'instruction_name','instruction_text']


class PictureSerializer(serializers.Serializer):
    picture = Base64ImageField(max_length=None, allow_empty_file=False)
