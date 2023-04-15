from rest_framework import serializers
from .models import *


class HandbookSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookSection
        fields = ['number', 'handbookPoints']


class HandbookPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookPoint
        fields = ['id', 'number', 'text', 'handbookSection', 'versionHistory']
