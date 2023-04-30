from django.db import models


class HandbookSection(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f"{self.number}"


class HandbookPoint(models.Model):
    number = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    handbookSection = models.ForeignKey(HandbookSection, on_delete=models.CASCADE, related_name="handbookPoints")

    def __str__(self):
        return f"{self.number}"


