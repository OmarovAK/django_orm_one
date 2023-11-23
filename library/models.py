from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    date_pub = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_pub']