from django.db import models
from djongo import models


# Create your models here.

class Author(models.model):
    class Meta:
        abstract = True

    name = models.CharField()


class Book(models.model):
    class Meta:
        abstract = True

    kind = models.CharField()
    api_book_id = models.CharField()
    title = models.CharField()
    authors = models.ArrayField(
        model_container=Author
    )
    publisher = models.CharField()
    publish_data = models.CharField()