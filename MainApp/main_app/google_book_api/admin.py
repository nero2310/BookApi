from django.contrib import admin

from .models import Book


# Register your models here.

class AdminBook(admin.ModelAdmin):
    pass


admin.site.register(Book, AdminBook)
