from django.forms import ModelForm
from .models import Book


class GoogleSearchForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'authors')
        success_url = '/book/details'
