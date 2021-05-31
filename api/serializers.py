from rest_framework import serializers
from .models import DigitalCurrency

class DigCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalCurrency
        fields = "__all__"