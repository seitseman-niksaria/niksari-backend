from .models import FurnitureModel
from rest_framework import viewsets
from niksari.serializers import FurnitureModelSerializer


class FurnitureModelViewSet(viewsets.ModelViewSet):
    queryset = FurnitureModel.objects.all()
    serializer_class = FurnitureModelSerializer