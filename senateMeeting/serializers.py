from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class SenateMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenateMeeting
        fields = ['number', 'announcement']


class SenatePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenatePoint
        fields = ['number', 'proposal', 'resolution', 'parent', 'senateMeeting']


class AnnexureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annexure
        fields = ['number', 'attachedPDF', 'senateMeeting']
