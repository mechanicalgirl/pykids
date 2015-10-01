from django.db import models

class Lesson(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Lesson %s: %s" % (self.number, self.name)


class Step(models.Model):
    lesson = models.ForeignKey(Lesson)
    step_number = models.IntegerField()
    step_name = models.CharField(max_length=200)
    header_title = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    audiocast = models.CharField(max_length=200, blank=True, null=True)
    screencast = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return "Lesson %s, Step %s: %s" % (self.lesson.number, self.step_number, self.step_name)
