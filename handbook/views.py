from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class HandbookSectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HandbookSection.objects.all().order_by('number')
    serializer_class = HandbookSectionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []


class HandbookPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HandbookPoint.objects.all().order_by('number')
    serializer_class = HandbookPointSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []


class GetHandbookPointsBySectionNumber(APIView):
    permission_classes = []

    def get(self, request):
        try:
            if "handbookSection" not in request.GET:
                return Response({"success": False,
                                 "message": "HandbookSection Number is Required!"},
                                status=status.HTTP_400_BAD_REQUEST)
            number = int(request.GET["handbookSection"])
            handbookSection = HandbookSection.objects.filter(number=number)[0]
        except HandbookSection.DoesNotExist:
            return Response({"success": False,
                             "message": "HandbookSection Not Found!"},
                            status=status.HTTP_404_NOT_FOUND)
        handbookPoints = handbookSection.handbookPoints.all()
        handbookPointsSerializer = HandbookPointSerializer(handbookPoints, many=True)
        return Response({"success": True,
                         "handbookPoints": handbookPointsSerializer.data},
                        status=status.HTTP_200_OK)

