from rest_framework import generics
from .models import *
from .serializers import *

class CurrentAffairsListAPIView(generics.ListAPIView):
    queryset = CurrentAffairs.objects.all()
    serializer_class = CurrentAffairsSerializer


