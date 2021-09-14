from django.shortcuts import render
from django.views.generic import DetailView

from .models import Author


# Create your views here.

class AuthorDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        AuthorModel = Author.objects.get(slug=slug)
        context = {
            'author_name' : AuthorModel.name,
            'biography': AuthorModel.biography,
            'birth_date': AuthorModel.birth_date,
            'death_date': AuthorModel.death_date,
        }
        return render(request, "authors/author_detail_view.html", context=context)
