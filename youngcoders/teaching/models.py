from django.db import models

class Step(models.Model):
    step_number = models.IntegerField()
    step_name = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return "Organizer Step %s: %s" % (self.step_number, self.step_name)
