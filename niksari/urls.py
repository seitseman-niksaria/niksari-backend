from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'furniture-models', views.FurnitureModelViewSet)
router.register(r'instructions', views.InstructionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("predict_model/", views.PictureRecognition.as_view(), name="picture")
]
