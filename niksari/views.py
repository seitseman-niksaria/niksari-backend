import statistics
from requests import Response
from .models import FurnitureModel, Instruction
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from niksari.serializers import FurnitureModelSerializer, InstructionSerializer, PictureSerializer
from . import prediction
from django.shortcuts import render
from django import forms


def index(request):
    return render(request, "niksari/index.html")


class FurnitureModelViewSet(viewsets.ModelViewSet):
    queryset = FurnitureModel.objects.all()
    serializer_class = FurnitureModelSerializer

class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer


# RestAPI for picture recognition
class PictureRecognition(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = PictureSerializer(data=request.data) #Create an instance of PictureSerializer with the request data
        if serializer.is_valid(): #Check if the picture is valid
            picture = serializer.validated_data["picture"]
            response = prediction.predict_image(picture) #Calling predict_image function in prediction.py
            return Response(response)
        else:
            print("ERROR:")
            print(serializer.errors)

