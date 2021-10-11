from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from authors.models import Author


# Create your models here.

class Book(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    kind = models.CharField(blank=True, max_length=100)
    api_book_id = models.CharField(blank=False, null=False, max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.CharField(blank=True, max_length=200)
    publish_data = models.DateField(blank=True, null=True)
    isbn = models.CharField(blank=True, max_length=13)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.api_book_id:
            raise ValueError("API_BOOK_ID Can't be null")

        if not self.slug:
            self.slug = slugify(self.api_book_id)
        super(Book, self).save(*args, **kwargs)


class Library(models.Model):
    slug = models.SlugField(unique=True)
    owner = models.OneToOneField(User, on_delete=models.PROTECT)
    books = models.ForeignKey(Book,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.owner)
