from django.test import TestCase
from .views import GoogleBookApi

# Create your tests here.

class GoogleBookApiUrlTest(TestCase):

    def test_search_url_without_parameter(self):
        book_1 = GoogleBookApi()
        book_1.search_parameters()
        self.assertEqual(book_1._get_query_url(),"https://www.googleapis.com/books/v1/volumes?q=") # Base url

    def test_search_url_with_parameter(self):
        book_1 = GoogleBookApi()
        book_1.search_parameters()
        self.assertHTMLEqual()
