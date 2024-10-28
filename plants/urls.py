from .api import *
from django.urls import path

urlpatterns = [
     path('api/plants/<int:id>/cares/', PlantCareView.as_view(), name='plant_care'),
     path('api/plants',PlantView.as_view(), name='plants'),
]