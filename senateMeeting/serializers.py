from rest_framework import serializers
from .models import *


class SenateMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenateMeeting
        fields = ['number', 'announcement', 'dateCreated', 'lastModified', 'senatePoints', 'annexures']


class SenatePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenatePoint
        fields = ['id', 'number', 'proposal', 'resolution', 'approvalComplete', 'approved', 'parent', 'subPoints', 'senateMeeting', 'handbookPointNewText', 'handbookPoint']


class AnnexureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annexure
        fields = ['number', 'attachedPDF', 'senateMeeting']
