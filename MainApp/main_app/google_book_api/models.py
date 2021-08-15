from django.db import models
from django.contrib.postgres.fields import ArrayField

import requests


# Create your models here.


class Book(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)
    kind = models.CharField(blank=True, max_length=100)
    api_book_id = models.CharField(blank=True, max_length=100)
    authors = ArrayField(
        models.TextField(blank=True),
        size=10
    )
    publisher = models.CharField(blank=True, max_length=200)
    publish_data = models.DateField(blank=True,null=True)
    api_url = ""

    def get_data(self):
        pass

    def search_parameters(self, **kwargs):
        pass

    def _get_query_url(self, title, author, publisher, subject, isbn, lccn, oclc):
        pass


class GoogleBookApi(Book):
    api_url = "https://www.googleapis.com/books/v1/volumes?q="
    query_parameters = {}

    def __init__(self, limit=200):
        '''

        :param limit: Limit results returning by get_data method
        '''
        self.limit = limit

    def get_data(self):
        if self.query_parameters:
            request = requests.get(self._get_query_url())
            if not "items" in request.json():
                raise ValueError("No results for search criteria")
            return {
              "items": request.json()["items"][:self.limit]
            }
        else:
            raise ValueError

    def search_parameters(self, **kwargs):
        self.query_parameters = {
            "title": kwargs.get("title", ''),
            "author": kwargs.get("author", ''),
            "publisher": kwargs.get("publisher", ''),
            "subject": kwargs.get("subject", ''),
            "isbn": kwargs.get("isbn", ''),
            "lccn": kwargs.get("lccn", ''),
            "oclc": kwargs.get("oclc", '')
        }

    def _get_query_url(self):
        parameters = self._add_search_criteria()
        print(self.api_url + parameters)
        return self.api_url + parameters

    def _add_search_criteria(self):
        search_criteria = ''
        for key, value in self.query_parameters.items():
            if value == '':
                continue
            if len(search_criteria) > 0:
                search_criteria += "+"
            if key == 'title':
                search_criteria += f"intitle:{value}"

            elif key == "author":
                search_criteria += f"inauthor:{value}"

            elif key == "publisher":
                search_criteria += f"inpublisher:{value}"

            else:
                search_criteria += f"{key}:{value}"
        return search_criteria
