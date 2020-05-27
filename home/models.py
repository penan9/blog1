from django.db import models


class Home(models.Model):
    filename = models.CharField(max_length=255)

    def __str__(self):
        return self.filename

    def snippet(self):
        return self.filename
