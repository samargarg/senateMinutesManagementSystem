from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from datetime import datetime, date, timedelta
from rest_framework import permissions, status

TEST_SENATE_MEETING_NUMBER = 99
TEST_SENATE_POINT_NUMBER = 99


class SenateMeetingTest(APITestCase):
    senatePointID = None

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
            "approved": True,
            "handbookPointNewText": "Test Edit Handbook Point Text",
            # "handbookPoint": "Test Edit Handbook Point"
        }
        response = self.client.put(f'/senateMeeting/senatePoints/{self.senatePointID}/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)
        self.assertTrue(response.json()["handbookPointNewText"] == "Test Edit Handbook Point Text")

    # TODO: Publish Handbook Test
