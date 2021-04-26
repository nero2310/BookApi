from django.shortcuts import render,HttpResponse
from django.views.generic import DetailView

import requests as rq


# Create your views here.

class BookDetail(DetailView):

    def get_context_data(self, **kwargs):
        return 0

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        response = rq.get("https://www.googleapis.com/books/v1/volumes?q=search+Witcher")
        print(response)
        return HttpResponse(response.json()["items"])

