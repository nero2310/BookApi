from django.db import models
from django.contrib.postgres.fields import ArrayField

import requests


# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100)
    kind = models.CharField(blank=True, max_length=100)
    api_book_id = models.CharField(blank=True, max_length=100)
    authors = models.JSONField()
    publisher = models.CharField(blank=True, max_length=200)
    publish_data = models.DateField(blank=True,null=True)
    api_url = ""

    def get_data(self):
        pass

    def search_parameters(self, **kwargs):
        pass

    def _get_query_url(self, title, author, publisher, subject, isbn, lccn, oclc):
        pass



