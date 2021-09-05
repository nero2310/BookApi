from django.db import models
from django.contrib.postgres.fields import ArrayField

import requests


# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True,null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=100)
    kind = models.CharField(blank=True, max_length=100)
    api_book_id = models.CharField(blank=True, max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.CharField(blank=True, max_length=200)
    publish_data = models.DateField(blank=True,null=True)
    isbn = models.CharField(blank=True,max_length=13)

    def __str__(self):
        return self.title
