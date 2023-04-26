from django.urls import path
from senateMeeting import *
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'senateMeetings', views.SenateMeetingViewSet)
router.register(r'senatePoints', views.SenatePointViewSet)
router.register(r'annexures', views.AnnexureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("getSenatePointsByMeetingNumber/", views.GetSenatePointsByMeetingNumber.as_view()),
    path("publishHandbook/", views.PublishHandbook.as_view()),
    path("getAgendaTabSenateMeetings/", views.GetAgendaTabSenateMeetings.as_view()),
    path("getSenateDecisionTabSenateMeetings/", views.GetSenateDecisionTabSenateMeetings.as_view()),
    path("getUpdateHandbookTabSenateMeetings/", views.GetUpdateHandbookTabSenateMeetings.as_view()),
]

