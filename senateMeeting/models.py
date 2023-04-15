from django.db import models


class SenateMeeting(models.Model):
    number = models.IntegerField(primary_key=True)
    announcement = models.CharField(max_length=512, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} Senate Meeting"


class SenatePoint(models.Model):
    number = models.IntegerField(primary_key=True)
    proposal = models.CharField(max_length=512, blank=True, null=True)
    resolution = models.CharField(max_length=512, blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subPoints", null=True, blank=True)
    isApproved = models.BooleanField(blank=True, null=True)

    senateMeeting = models.ForeignKey(SenateMeeting, on_delete=models.CASCADE, related_name="senatePoints")

    def __str__(self):
        return f"{self.number}: {self.proposal}"


class Annexure(models.Model):
    number = models.IntegerField(primary_key=True)
    attachedPDF = models.FileField(upload_to="annexures/", default=None, null=True)
    senateMeeting = models.ForeignKey(SenateMeeting, on_delete=models.CASCADE, related_name="attachedAnnexures")

    def __str__(self):
        return f"Annexure {self.number}"

