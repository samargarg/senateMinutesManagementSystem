from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from datetime import datetime, date, timedelta
from rest_framework import permissions, status
from django.contrib.auth import get_user_model

User = get_user_model()

TEST_SENATE_MEETING_NUMBER = 99
TEST_SENATE_POINT_NUMBER = 99


class SenateMeetingTest(APITestCase):
    senatePointID = None

    def setUp(self):
        self.user = User.objects.create_superuser(username='tester', password='test')
        self.client.force_authenticate(user=self.user)

    def testCreateNewSenateMeeting(self):
        data = {
            "number": TEST_SENATE_MEETING_NUMBER,
            "announcement": "Test Announcement"
        }
        response = self.client.post('/senateMeeting/senateMeetings/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)
        self.assertTrue("number" in response.json())

    def testCreateNewSenatePoint(self):
        self.testCreateNewSenateMeeting()
        data = {
            "number": 1,
            "proposal": "Test Proposal",
            "senateMeeting": TEST_SENATE_MEETING_NUMBER
        }
        response = self.client.post('/senateMeeting/senatePoints/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)
        self.assertTrue("id" in response.json())
        self.senatePointID = int(response.json()['id'])

    def testEditSenateMeeting(self):
        self.testCreateNewSenateMeeting()
        data = {
            "number": TEST_SENATE_MEETING_NUMBER,
            "announcement": "Test Edit Announcement"
        }
        response = self.client.put(f'/senateMeeting/senateMeetings/{TEST_SENATE_MEETING_NUMBER}/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)
        self.assertTrue(response.json()["announcement"] == "Test Edit Announcement")

    def testEditSenatePoint(self):
        self.testCreateNewSenatePoint()
        data = {
            "number": 1,
            "proposal": "Test Edit Proposal",
            "resolution": "Test Edit Resolution",
            "senateMeeting": TEST_SENATE_MEETING_NUMBER,
            "approveComplete": True,
            "approved": 2,
            "handbookPointNewText": "Test Edit Handbook Point Text",
            # "handbookPoint": "Test Edit Handbook Point"
        }
        response = self.client.put(f'/senateMeeting/senatePoints/{self.senatePointID}/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)
        self.assertTrue(response.json()["handbookPointNewText"] == "Test Edit Handbook Point Text")

    def testDeleteSenateMeeting(self):
        self.testCreateNewSenateMeeting()
        response = self.client.delete(f'/senateMeeting/senateMeetings/{TEST_SENATE_MEETING_NUMBER}/')
        self.assertTrue(response.status_code == status.HTTP_204_NO_CONTENT)

    def testDeleteSenatePoint(self):
        self.testCreateNewSenatePoint()
        response = self.client.delete(f'/senateMeeting/senatePoints/{self.senatePointID}/')
        self.assertTrue(response.status_code == status.HTTP_204_NO_CONTENT)

    def testReadSenateMeeting(self):
        response = self.client.get(f'/senateMeeting/senateMeetings/')
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def testReadSenatePoint(self):
        response = self.client.get(f'/senateMeeting/senatePoints/')
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def testGetSenatePointsByMeetingNumber(self):
        self.testCreateNewSenateMeeting()
        response = self.client.get(f'/senateMeeting/getSenatePointsByMeetingNumber/?senateMeeting={TEST_SENATE_MEETING_NUMBER}')
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    # TODO: Need to be connected to handbook test
    def testPublishHandbook(self):
        self.testCreateNewSenatePoint()
        data = {
            "senateMeeting": TEST_SENATE_MEETING_NUMBER,
        }
        response = self.client.post(f'/senateMeeting/publishHandbook/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)
