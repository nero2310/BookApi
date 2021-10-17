from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .forms import GoogleSearchForm
from .models import Library

import requests as rq


# Create your views here.

class BookDetail(DetailView):

    def get(self, request, *args, **kwargs):
        form = GoogleSearchForm()
        context = {'form': form}
        return render(request, "google_book_api/search_form.html", context)

    def post(self, request):
        QueryGenerator = ApiQueryGenerator(**request.POST)
        url = QueryGenerator.generate_query()
        context = data_fetch_from_api(url)
        return render(request, "google_book_api/search_results.html", context)


class LibraryDetail(DetailView):
    model = Library

    def get(self, request):
        if request.user.is_authenticated:
            library = get_object_or_404(Library, owner__username=request.user.username)
            return render(request, "google_book_api/user_library.html", {'library': library})
        else:
            return redirect('user_auth:login_view')

class ApiQueryGenerator:
    base_api_url = "https://www.googleapis.com/books/v1/volumes?q="
    aliases = {
        "title": "intitle",
        "authors": "inauthor",
        "publisher": "inpublisher"
    }

    def __init__(self, **kwargs):
        self.query_parameters = {
            "title": kwargs.get("title", ''),
            "authors": kwargs.get("authors", ''),
            "publisher": kwargs.get("publisher", ''),
            "subject": kwargs.get("subject", ''),
            "isbn": kwargs.get("isbn", ''),
            "lccn": kwargs.get("lccn", ''),
            "oclc": kwargs.get("oclc", '')
        }

    def generate_query(self):
        query = ''
        for key, value in self.query_parameters.items():
            if value == '' or any(value) == False:
                continue
            if len(query) > 0:
                query += "+"
            if isinstance(value, list):
                for element in value:
                    query += self.aliases.get(key) + f":{element}"
                    query += "+"
                query = query[:-1]
                continue
            if key in self.aliases:
                query += self.aliases.get(key) + f":{value}"
            else:
                query += f"{key}: {value}"
        return self.base_api_url + query


def data_fetch_from_api(url):
    data = rq.get(url)
    if not "items" in data.json():
        raise ValueError("No results for search ctiteria")
    return {
        "items": data.json()["items"]
    }
