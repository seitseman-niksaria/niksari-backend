from .models import FurnitureModel, Instruction
from rest_framework import viewsets
from niksari.serializers import FurnitureModelSerializer, InstructionSerializer
from . import prediction
from django.shortcuts import render

def index(request):
    return render(request, "niksari/index.html")


class FurnitureModelViewSet(viewsets.ModelViewSet):
    queryset = FurnitureModel.objects.all()
    serializer_class = FurnitureModelSerializer

class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer

# Predict image using prediction.py
def predict_from_upload(request):
    users_image = request.FILES["image"]
    response = prediction.predict_image(users_image)
    predicted_result = {"class_name": response}
    return render(request, "niksari/index.html", predicted_result)