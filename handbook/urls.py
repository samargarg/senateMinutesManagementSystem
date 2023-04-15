from django.urls import path
from senateMeeting import *
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'handbookSections', views.HandbookSectionViewSet)
router.register(r'handbookPoints', views.HandbookPointViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("getHandbookPointsBySectionNumber/", views.GetHandbookPointsBySectionNumber.as_view()),
]
