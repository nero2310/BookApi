from django.contrib import admin

from .models import Book,Library


# Register your models here.

class AuthorToBookInline(admin.StackedInline):
    model = Book.authors.through


class AdminBook(admin.ModelAdmin):
    filter_horizontal = ('authors',)
    prepopulated_fields = {"slug":["api_book_id"]}


class AdminAuthor(admin.ModelAdmin):
    inlines = [
        AuthorToBookInline
    ]


admin.site.register(Book, AdminBook)
admin.site.register(Library)
