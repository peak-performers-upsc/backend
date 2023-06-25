from rest_framework import serializers
from . models import *

class CurrentAffairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentAffairs
        fields = ["Content"]
