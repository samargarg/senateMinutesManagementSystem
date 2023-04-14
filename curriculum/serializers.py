from rest_framework import serializers
from .models import *


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ['program', 'batch', 'branch', 'senateMeeting']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['number', 'curriculum']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code', 'name', 'credits', 'nature', 'type', 'preRequisites', 'contents', 'references', 'objectives',
                  'justification', 'semester']

