from rest_framework import serializers
from .models import *


class SenateMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenateMeeting
        fields = ['number', 'announcement', 'dateCreated', 'lastModified', 'senatePoints', 'annexures', 'agendaFinalised', 'resolutionFinalised', 'published']


class SenatePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenatePoint
        fields = ['id', 'number', 'name', 'proposal', 'resolution', 'approvalComplete', 'approved', 'parent', 'subPoints', 'senateMeeting', 'handbookPointNewText', 'handbookPoint']


class AnnexureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annexure
        fields = ['id', 'number', 'attachedPDF', 'senateMeeting']
