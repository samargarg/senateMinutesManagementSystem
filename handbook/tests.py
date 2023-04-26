from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from datetime import datetime, date, timedelta
from rest_framework import permissions, status

TEST_SENATE_MEETING_NUMBER = 99
TEST_SENATE_POINT_NUMBER = 99
TEST_HANDBOOK_SECTION_NUMBER = 99
TEST_HANDBOOK_POINT_NUMBER = 99


class HandbookTest(APITestCase):
    senatePointID = None

    def testCreateNewHandbookSection(self):
        data = {
            "number": TEST_HANDBOOK_SECTION_NUMBER,
            "name": "Test Name"
        }
        response = self.client.post('/handbook/handbookSections/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)
        self.assertTrue("number" in response.json())

    def testCreateNewHandbookPoint(self):
        self.testCreateNewHandbookSection()
        data = {
            "number": TEST_HANDBOOK_POINT_NUMBER,
            "text": "Test Text",
            "handbookSection": TEST_HANDBOOK_SECTION_NUMBER
        }
        response = self.client.post('/handbook/handbookPoints/', data)
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)
        self.assertTrue("number" in response.json())
