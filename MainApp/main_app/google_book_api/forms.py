from django import forms


class GoogleSearchForm(forms.Form):
    title = forms.CharField(label="title", max_length=100, required=True)
    author = forms.CharField(label="author", max_length=100, required=False)
