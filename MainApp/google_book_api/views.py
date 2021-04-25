from django.shortcuts import render
from django.views.generic import DetailView


# Create your views here.

class BookDetail(DetailView):

    def get_context_data(self, **kwargs):
        return 0
