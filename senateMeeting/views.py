from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class SenateMeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SenateMeeting.objects.all().order_by('lastModified')
    serializer_class = SenateMeetingSerializer
    permission_classes = [permissions.IsAuthenticated]


class SenatePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SenatePoint.objects.all().order_by('number')
    serializer_class = SenatePointSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnnexureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Annexure.objects.all().order_by('number')
    serializer_class = AnnexureSerializer
    permission_classes = [permissions.IsAuthenticated]
