from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *


class CurriculumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Curriculum.objects.all().order_by('senateMeeting__dateCreated')
    serializer_class = CurriculumSerializer
    permission_classes = []


class SemesterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Semester.objects.all().order_by('curriculum__program', 'curriculum__batch', 'curriculum__branch',
                                               'number')
    serializer_class = SemesterSerializer
    permission_classes = []


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('code')
    serializer_class = CourseSerializer
    permission_classes = []
