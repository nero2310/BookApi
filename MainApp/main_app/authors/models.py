from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name