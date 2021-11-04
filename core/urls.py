from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .viewsets import TicketViewSet, DeviceViewSet

router = routers.DefaultRouter()
router.register(r'ticket', TicketViewSet)
router.register(r'device', DeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]