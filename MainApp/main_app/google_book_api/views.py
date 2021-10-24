from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView

from .forms import GoogleSearchForm
from .models import Library, Book

import requests as rq


# Create your views here.

class BookSearch(View):  # toDo Verify if DetailView is need

    def get(self, request, *args, **kwargs):
        form = GoogleSearchForm()
        context = {'form': form}
        return render(request, "google_book_api/search_form.html", context)

    def post(self, request):
        QueryGenerator = ApiQueryGenerator(**request.POST)
        url = QueryGenerator.generate_query()
        context = data_fetch_from_api(url)
        return render(request, "google_book_api/search_results.html", context)


class BookDetailView(DetailView):
    template_name = 'google_book_api/book_detail.html'
    template_name_field = 'book'
    model = Book


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
    url = None

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

    def generate_query(self, start_index=0, max_results=10):
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
        self.url = self.base_api_url + query
        return self.url

    def pagination(self, start_index, max_results=10):
        if self.url.rfind("&startIndex") == -1:  # rfind return -1 if value not found
            self.url += f"&startIndex={start_index}&maxResults={max_results}"
            return self.url
        else:  # Not implemented yet
            raise NotImplementedError


def data_fetch_from_api(url):
    data = rq.get(url)
    if "items" in data.json():
        return {
            "items": data.json()["items"]
        }
    raise ValueError("No results for search ctiteria")
