from django.db import models

class Page(models.Model):
    page_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "%s" % (self.page_name)
