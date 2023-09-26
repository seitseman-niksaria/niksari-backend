from django.shortcuts import render, get_object_or_404
from .models import FurnitureModel


# List of all avaible furniture models
def index(request):
    ### CHANGE TO GET_OGBJECT_OR_404
    furniture_model_list = FurnitureModel.objects.order_by("furniture_name")
    context = {
        "furniture_model_list": furniture_model_list,
    }
    return render(request, "niksari/index.html", context)


# Details for a specific furniture model by id
def furniture_detail(request, furniture_model_id):
    furniture_model = get_object_or_404(FurnitureModel, pk=furniture_model_id)
    return render(request, "niksari/detail.html", {"furniture_model": furniture_model})
