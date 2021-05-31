from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DigCurrencySerializer
from .models import DigitalCurrency
from .permissions import IsSuperuserOrStaffReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class DigCurrencyViewSet(viewsets.ModelViewSet):
    queryset = DigitalCurrency.objects.all()
    serializer_class = DigCurrencySerializer
    filterset_fields = ['name', 'short_name']
    search_fields = ['name', 'short_name']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsSuperuserOrStaffReadOnly]
        return [permission() for permission in permission_classes]