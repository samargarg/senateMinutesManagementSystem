from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from datetime import datetime, date, timedelta
from rest_framework import permissions, status
from django.contrib.auth import get_user_model

User = get_user_model()


TEST_SENATE_MEETING_NUMBER = 99
TEST_SENATE_POINT_NUMBER = 99
TEST_HANDBOOK_SECTION_NUMBER = 99
TEST_HANDBOOK_POINT_NUMBER = 99


class HandbookTest(APITestCase):
    handbookPointID = None

    def setUp(self):
        self.user = User.objects.create_superuser(username='tester', password='test')
        self.client.force_authenticate(user=self.user)

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
        self.handbookPointID = int(response.json()['id'])

    def testDeleteHandbookSection(self):
        self.testCreateNewHandbookSection()
        response = self.client.delete(f'/handbook/handbookSections/{TEST_HANDBOOK_SECTION_NUMBER}/')
        print(response)
        self.assertTrue(response.status_code == status.HTTP_204_NO_CONTENT)

    def testDeleteHandbookPoint(self):
        self.testCreateNewHandbookPoint()
        response = self.client.delete(f'/handbook/handbookPoints/{self.handbookPointID}/')
        print(response)
        self.assertTrue(response.status_code == status.HTTP_204_NO_CONTENT)

    def testReadHandbookSection(self):
        response = self.client.get(f'/handbook/handbookSections/')
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def testReadHandbookPoint(self):
        response = self.client.get(f'/handbook/handbookPoints/')
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def testGetHandbookPointsBySectionNumber(self):
        self.testCreateNewHandbookPoint()
        response = self.client.get(
            f'/handbook/getHandbookPointsBySectionNumber/?handbookSection={TEST_HANDBOOK_SECTION_NUMBER}')
        print(response.json())
        self.assertTrue(response.status_code == status.HTTP_200_OK)