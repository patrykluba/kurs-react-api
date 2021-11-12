from rest_framework import serializers
from .models import Ticket, Device


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data['owner'] = self.context['request'].user.id
        return super(DeviceSerializer, self).to_internal_value(data)


    class Meta:
        model = Device
        fields = '__all__'