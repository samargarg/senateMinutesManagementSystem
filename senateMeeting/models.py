from django.db import models
from handbook.models import HandbookPoint


class SenateMeeting(models.Model):
    number = models.IntegerField(primary_key=True)
    announcement = models.CharField(max_length=512, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} Senate Meeting"


class SenatePoint(models.Model):
    number = models.CharField(max_length=2)
    proposal = models.CharField(max_length=512, blank=True, null=True)
    resolution = models.CharField(max_length=512, blank=True, null=True)
    approvalComplete = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subPoints", null=True, blank=True)
    senateMeeting = models.ForeignKey(SenateMeeting, on_delete=models.CASCADE, related_name="senatePoints")
    handbookPointNewText = models.TextField(blank=True, null=True)
    handbookPoint = models.ForeignKey(HandbookPoint, on_delete=models.CASCADE, blank=True, null=True)
    handbookPointConfirmed = models.ForeignKey(HandbookPoint, on_delete=models.CASCADE, related_name="versionHistory", blank=True, null=True)

    def __str__(self):
        return f"{self.number}: {self.proposal}"


class Annexure(models.Model):
    number = models.IntegerField(primary_key=True)
    attachedPDF = models.FileField(upload_to="annexures/", default=None, null=True)
    senateMeeting = models.ForeignKey(SenateMeeting, on_delete=models.CASCADE, related_name="annexures")

    def __str__(self):
        return f"Annexure {self.number}"

