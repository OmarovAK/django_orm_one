from django.db import models


class Phones(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.id}"

    class Meta:
        ordering = ['id']



