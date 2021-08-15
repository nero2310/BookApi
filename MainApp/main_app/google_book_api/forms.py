from django.forms import ModelForm
from .views import GoogleBookApi


class GoogleSearchForm(ModelForm):
    class Meta:
        model = GoogleBookApi
        fields = ('title', 'authors')
        success_url = '/book/details'
