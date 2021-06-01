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
        context = {'0': 0}
        return render(request, "google_book_api/search_results.html", context)
