from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'furniture-models', views.FurnitureModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('predict_from_upload/', views.predict_from_upload, name='predict_from_upload'),
    path("", views.index, name="index"),
]
