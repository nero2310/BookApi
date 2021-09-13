from django.contrib import admin

from google_book_api.models import Book
from .models import Author


# Register your models here.

class AuthorToBookInline(admin.StackedInline):
    model = Book.authors.through


class AdminAuthor(admin.ModelAdmin):
    inlines = [
        AuthorToBookInline
    ]
    prepopulated_fields = {"slug":["name"]}



admin.site.register(Author, AdminAuthor)
