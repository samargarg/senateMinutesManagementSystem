from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from handbook.models import *
from handbook.serializers import HandbookPointSerializer


class SenateMeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SenateMeeting.objects.all().order_by('lastModified')
    serializer_class = SenateMeetingSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []


class SenatePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SenatePoint.objects.all().order_by('number')
    serializer_class = SenatePointSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []

class AnnexureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Annexure.objects.all().order_by('number')
    serializer_class = AnnexureSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []


class GetSenatePointsByMeetingNumber(APIView):
    permission_classes = []
    def get(self, request):
        try:
            if "senateMeeting" not in request.GET:
                return Response({"success": False,
                                 "message": "SenateMeeting Number is Required!"},
                                status=status.HTTP_400_BAD_REQUEST)
            number = int(request.GET["senateMeeting"])
            senateMeeting = SenateMeeting.objects.filter(number=number)[0]
        except SenateMeeting.DoesNotExist:
            return Response({"success": False,
                             "message": "SenateMeeting Not Found!"},
                            status=status.HTTP_404_NOT_FOUND)
        senatePoints = senateMeeting.senatePoints.all()
        senatePointsSerializer = SenatePointSerializer(senatePoints, many=True)
        return Response({"success": True,
                         "senatePoints": senatePointsSerializer.data},
                        status=status.HTTP_200_OK)


class PublishHandbook(APIView):
    permission_classes = []

    def post(self, request):
        try:
            if "senateMeeting" not in request.POST:
                return Response({"success": False,
                                 "message": "SenateMeeting Number is Required!"},
                                status=status.HTTP_400_BAD_REQUEST)
            number = int(request.POST["senateMeeting"])

            senateMeeting = SenateMeeting.objects.filter(number=number)[0]
        except SenateMeeting.DoesNotExist:
            return Response({"success": False,
                             "message": "SenateMeeting Not Found!"},
                            status=status.HTTP_404_NOT_FOUND)

        senatePoints = senateMeeting.senatePoints.all()

        for senatePoint in senatePoints:
            if senatePoint.handbookPoint is None:
                continue
            print(senatePoint.handbookPoint)
            senatePoint.handbookPoint.text = senatePoint.handbookPointNewText
            senatePoint.handbookPoint.save()

        handbookPoints = HandbookPoint.objects.all()
        handbookPointsSerializer = HandbookPointSerializer(handbookPoints, many=True)
        return Response({"success": True,
                         "handbookPoints": handbookPointsSerializer.data},
                        status=status.HTTP_200_OK)
