from django.utils.text import slugify

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Author must have a name")

        if not self.slug:
            self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)
