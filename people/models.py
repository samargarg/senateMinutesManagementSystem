from django.db import models

class People(models.Model):
    class Position(models.IntegerChoices):
        Default = 0, 'Default'

    name = models.CharField(max_length=50)
    position = models.PositiveSmallIntegerField(choices=Position.choices)
    isStudent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.Position.choices[self.position][1]})"
