from .views import *
from django.urls import path,include

urlpatterns = [
    path('all/',CurrentAffairsListAPIView.as_view(),name="CurrentAffairsListAPIView"),
]