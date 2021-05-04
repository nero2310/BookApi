from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView

from .models import GoogleBookApi


# Create your views here.

class BookDetail(DetailView):

    def get_context_data(self, **kwargs):
        return 0

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        book_1 = GoogleBookApi()
        book_1.search_parameters(title="Witcher", author="Sapek", publisher="", subject="", isbn="", lccn="", oclc="")
        data = book_1.get_data()
        # print(data)
        return HttpResponse(data)
