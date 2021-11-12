from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Ticket, Device
from .serializers import TicketSerializer, DeviceSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(author=user)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Device.objects.all()
        else:
            return Device.objects.filter(owner=user)
