from django.db import models
from senateMeeting.models import SenateMeeting


class Curriculum(models.Model):
    class Branch(models.IntegerChoices):
        COMMON = 0, 'Common To All'
        CS = 1, 'Computer Science'
        EE = 2, 'Electrical'
        CE = 3, 'Civil',
        CH = 4, 'Chemical'

    class Program(models.IntegerChoices):
        BTECH = 0, 'B. Tech'
        MTECH = 1, 'M. Tech.'
        MDES = 2, 'M. Design'

    program = models.PositiveSmallIntegerField(choices=Program.choices)
    batch = models.IntegerField()
    branch = models.PositiveSmallIntegerField(choices=Branch.choices)
    senateMeeting = models.ForeignKey(SenateMeeting, on_delete=models.DO_NOTHING, related_name="introducedCurriculums")

    def __str__(self):
        return f"{self.Program.choices[self.program][1]} {self.batch} {self.Branch.choices[self.branch][1]}"


class Semester(models.Model):
    class SemesterChoices(models.IntegerChoices):
        I = 0, 'FIRST'
        II = 1, 'SECOND'
        III = 2, 'THIRD'
        IV = 3, 'FOURTH',
        V = 4, 'FIFTH'
        VI = 5, 'SIXTH'
        VII = 6, 'SEVENTH'
        VIII = 7, 'EIGHTH'

    number = models.PositiveSmallIntegerField(choices=SemesterChoices.choices)
    curriculum = models.ForeignKey("Curriculum", on_delete=models.CASCADE, related_name="semesters")

    def __str__(self):
        return f"{self.SemesterChoices.choices[self.number][1]} ({self.curriculum})"


class Course(models.Model):
    # TODO Add the choices
    class Type(models.IntegerChoices):
        Default = 0, 'Default'

    # TODO Add the choices
    class Nature(models.IntegerChoices):
        Default = 0, 'Default'

    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    credits = models.IntegerField()
    nature = models.PositiveSmallIntegerField(choices=Nature.choices)
    type = models.PositiveSmallIntegerField(choices=Type.choices)
    preRequisites = models.ManyToManyField("self", related_name="preRequisiteOf", symmetrical=False, blank=True, null=True)
    contents = models.CharField(max_length=512, blank=True, null=True)
    references = models.CharField(max_length=512, blank=True, null=True)
    objectives = models.CharField(max_length=512, blank=True, null=True)
    justification = models.CharField(max_length=512, blank=True, null=True)
    semester = models.ManyToManyField(Semester, related_name="courses")

    def __str__(self):
        return f"{self.code}: {self.name}"


