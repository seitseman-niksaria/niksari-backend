from django.urls import path

from . import views

urlpatterns = [
    # ex: /niksari/
    path("", views.index, name="index"),
    # ex: /niksari/1/
    path("<int:furniture_model_id>/", views.furniture_detail, name="furniture_detail"),
]
