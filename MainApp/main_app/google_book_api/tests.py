from django.test import TestCase, Client
from .views import SearchBooksGoogleApi
from .forms import GoogleSearchForm


# Create your tests here.


class QueryLinkGenerationTest(TestCase):

    def test_query_without_parameters(self):
        test = SearchBooksGoogleApi()
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=")

    def test_query_with_title(self):
        test = SearchBooksGoogleApi(**{"title": "Witcher"})
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=intitle:Witcher")

    def test_query_with_author(self):
        test = SearchBooksGoogleApi(**{"author": "Martin"})
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=inauthor:Martin")


class BookSearchFormTest(TestCase):

    def test_form_with_title(self):
        form = GoogleSearchForm(data={"title": "Witcher"})
        self.assertEqual(form.errors, {})  # If no error occur then form.error return empty dict

    def test_form_without_data(self):
        form = GoogleSearchForm(data={})
        self.assertEqual(form.errors, {"title": ["This field is required."]})

    def test_form_one_author(self):
        form = GoogleSearchForm(data={"title": "Game of throne",
                                      "author": "R.R Marting"})
        self.assertEqual(form.errors, {})

    def test_form_multiple_authors(self):
        form = GoogleSearchForm(data={"title": "Game of throne",
                                      "author": ["R.R Marting", "J.K Rowling"]})
        self.assertEqual(form.errors, {})


class BookClassTest(TestCase):

    def setUp(self):
        pass


class TestPagination(TestCase):

    def test_base_pagination(self):
        test = SearchBooksGoogleApi(**{"title": "Witcher"})
        generated_url = test.generate_query()
        self.assertEqual(test.pagination(generated_url, 0),
                         'https://www.googleapis.com/books/v1/volumes?q=intitle:Witcher&startIndex=0&maxResults=10')
        self.assertEqual(test.pagination(generated_url, 2),
                 'https://www.googleapis.com/books/v1/volumes?q=intitle:Witcher&startIndex=10&maxResults=10')


    def test_pagination_with_nonstandard_maxResultValue(self):
        test = SearchBooksGoogleApi(**{"title": "Witcher"})
        generated_url = test.generate_query()
        self.assertEqual(test.pagination(generated_url, 2, 15),
                         'https://www.googleapis.com/books/v1/volumes?q=intitle:Witcher&startIndex=15&maxResults=15')

    def test_pagination_negative_page(self):
        test = SearchBooksGoogleApi(**{"title": "Witcher"})
        generated_url = test.generate_query()
        self.assertEqual(test.pagination(generated_url, -1, 15),
                         'https://www.googleapis.com/books/v1/volumes?q=intitle:Witcher&startIndex=0&maxResults=15')
