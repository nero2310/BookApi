from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, DetailView
from django.http import Http404

from .forms import GoogleSearchForm
from .models import Library, Book

import requests as rq


# Create your views here.

def book_search(request):
    if request.method == 'POST':
        form = GoogleSearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            query = {
                'title': cd['title']
            }
            if cd.get('author','') != '':
                query['author'] = cd['author']
            return redirect(reverse('search_results',kwargs = query))
    form = GoogleSearchForm()
    context = {'form': form}
    return render(request, "google_book_api/search_form.html", context)

def book_search_results(request, **kwargs):
    query = {
        'title': kwargs.get('title', ''),
        'author': kwargs.get('author', ''),
    }
    QueryGenerator = ApiQueryGenerator(**query)
    url = QueryGenerator.generate_query()
    context = data_fetch_from_api(url)
    page = 1
    return render(request, "google_book_api/search_results.html", {
        'books': context,
        'page': page
    })


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
            "oclc": kwargs.get("oclc", ''),
        }
        self.current_page = kwargs.get("page",1)

    def generate_query(self, max_results=10):
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

    def pagination(self, url, page, max_results=10):
        if page < 1: # Not allowing for negative/zero pages
            page = 1
        if url.rfind("&startIndex") == -1:  # rfind return -1 if value not found
            url += f"&startIndex={(page - 1)* max_results}&maxResults={max_results}"
            return url


def data_fetch_from_api(url):
    data = rq.get(url)
    if "items" in data.json():
        return {
            "items": data.json()["items"]
        }
    raise Http404("No results for search ctiteria")
