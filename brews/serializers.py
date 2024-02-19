from rest_framework import serializers
from .models import Brew

class BrewSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id","owner","name","brew_type","brewery", "description","created_at", "updated_at")
    model = Brew