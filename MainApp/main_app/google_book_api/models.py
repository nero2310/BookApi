from django.db import models
from djongo import models as dj


# Create your models here.

class Author(models.Model):
    class Meta:
        abstract = True

    name = models.CharField()


class Book(models.Model):
    class Meta:
        abstract = True

    kind = models.CharField()
    api_book_id = models.CharField()
    title = models.CharField()
    authors = dj.ArrayField(
        model_container=Author
    )
    publisher = models.CharField()
    publish_data = models.CharField()
    api_url = ""

    def get_data(self):
        pass

    def _get_query_url(self, title, author, publisher, subject, isbn, lccn, oclc):
        pass


class GoogleBookApi(Book):

    api_url = "https://www.googleapis.com/books/v1/volumes?q="

    def get_data(self):
        pass

    def _get_query_url(self, title, author, publisher, subject, isbn, lccn, oclc):
        parameters = f"intitle={title}+inauthor={author}+inpublisher{publisher}+" \
                     f"subject={subject}+isbn{isbn}+lccn{lccn}+oclc{oclc}"
        return self.api_url+parameters
