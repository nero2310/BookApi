from django.forms import ModelForm
from .views import GoogleBookApi

class GoogleSearchForm(ModelForm):
    class Meta:
        model = GoogleBookApi
        fields = '__all__'
        success_url = '/book/details'