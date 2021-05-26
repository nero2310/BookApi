from django.db import models
from djongo import models as dj

import requests


# Create your models here.

class Author(models.Model):
    class Meta:
        abstract = True

    name = models.TextField()


class Book(models.Model):
    class Meta:
        abstract = True

    kind = models.TextField()
    api_book_id = models.TextField()
    title = models.TextField()
    authors = dj.ArrayField(
        model_container=Author
    )
    publisher = models.TextField()
    publish_data = models.TextField()
    api_url = ""

    def get_data(self):
        pass

    def search_parameters(self, **kwargs):
        pass

    def _get_query_url(self, title, author, publisher, subject, isbn, lccn, oclc):
        pass

    def _limit_search_results(self,data,limit = 200):
        pass


class GoogleBookApi(Book):
    api_url = "https://www.googleapis.com/books/v1/volumes?q="
    query_parameters = {}

    def get_data(self):
        if self.query_parameters:
            request = requests.get(self._get_query_url())
            request.json()["items"] == self._limit_search_results(request.json())
            return request.json()["items"]
        else:
            raise ValueError

    def _limit_search_results(self,data,limit = 1):
        return data["items"][0:limit]

    def search_parameters(self, **kwargs):
        self.query_parameters = {
            "title": kwargs.get("title", ''),
            "author": kwargs.get("author",''),
            "publisher": kwargs.get("publisher",''),
            "subject": kwargs.get("subject", ''),
            "isbn": kwargs.get("isbn",''),
            "lccn": kwargs.get("lccn",''),
            "oclc": kwargs.get("oclc",'')
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
            if len(search_criteria)>0:
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