from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView

from .models import GoogleBookApi

from .forms import GoogleSearchForm


# Create your views here.

class BookDetail(DetailView):

    def get_context_data(self, **kwargs):
        return 0

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        form = GoogleSearchForm()
        context = {'form': form}
        return render(request, "google_book_api/search_form.html", context)

    def post(self, request):
        BookApi = GoogleBookApi()
        BookApi.search_parameters(**request.POST)
        context = BookApi.get_data()
        print(context)
        return render(request, "google_book_api/search_results.html", context)


class ApiQueryGenerator:
    base_api_url = "https://www.googleapis.com/books/v1/volumes?q="
    aliases = {
        "title": "intitle",
        "author": "inauthor",
        "publisher": "inpublisher"
    }

    def __init__(self, **kwargs):
        self.query_parameters = {
            "title": kwargs.get("title", ''),
            "author": kwargs.get("author", ''),
            "publisher": kwargs.get("publisher", ''),
            "subject": kwargs.get("subject", ''),
            "isbn": kwargs.get("isbn", ''),
            "lccn": kwargs.get("lccn", ''),
            "oclc": kwargs.get("oclc", '')
        }

    def generate_query(self):
        query = ''
        for key, value in self.query_parameters.items():
            if value == '':
                continue
            if len(query) > 0:
                query += "+"
            if key in self.aliases:
                query += self.aliases.get(key) + f":{value}"
            else:
                query += f"{key}: {value}"
        return self.base_api_url + query
