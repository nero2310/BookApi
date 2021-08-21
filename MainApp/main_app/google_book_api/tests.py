from django.test import TestCase,Client
from .views import GoogleBookApi,ApiQueryGenerator

# Create your tests here.

class GoogleBookApiUrlTest(TestCase):

    def test_search_url_without_parameter(self):
        book_1 = GoogleBookApi()
        book_1.search_parameters()
        self.assertEqual(book_1._get_query_url(),"https://www.googleapis.com/books/v1/volumes?q=") # Base url

    def test_search_url_with_parameter(self):
        book_1 = GoogleBookApi()
        book_1.search_parameters()
        self.assertHTMLEqual("","")

class GoogleBookApiClientTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_method(self):
        response = self.client.get('/book/detail')
        self.assertTrue(response.status_code == 301)

    def test_post_method(self):
        response = self.client.post('/book/detail')
        self.assertEqual(response.status_code,301)

class QueryLinkGenerationTest(TestCase):


    def test_query_without_parameters(self):
        test = ApiQueryGenerator()
        url = test.generate_query()
        self.assertEqual(url,"https://www.googleapis.com/books/v1/volumes?q=")

    def test_query_with_authors(self):
        test = ApiQueryGenerator(**{"author":"Martin"})
        url = test.generate_query()
        self.assertEqual(url,"https://www.googleapis.com/books/v1/volumes?q=inauthor:Martin")
