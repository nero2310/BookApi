from django.test import TestCase, Client
from .views import ApiQueryGenerator
from .forms import GoogleSearchForm


# Create your tests here.


class GoogleBookApiClientTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_method(self):
        response = self.client.get('/book/detail')
        self.assertTrue(response.status_code == 301)

    def test_post_method(self):
        response = self.client.post('/book/detail')
        self.assertEqual(response.status_code, 301)


class QueryLinkGenerationTest(TestCase):

    def test_query_without_parameters(self):
        test = ApiQueryGenerator()
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=")

    def test_query_with_title(self):
        test = ApiQueryGenerator(**{"title":"Witcher"})
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=intitle:Witcher")

    def test_query_with_author(self):
        test = ApiQueryGenerator(**{"authors": "Martin"})
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=inauthor:Martin")

    def test_query_with_multiple_authors(self):
        test = ApiQueryGenerator(**{"authors":["A","B","C"]})
        url = test.generate_query()
        self.assertEqual(url, "https://www.googleapis.com/books/v1/volumes?q=inauthor:A+inauthor:B+inauthor:C")

class BookSearchFormTest(TestCase):

    def test_form_with_title(self):
        form = GoogleSearchForm(data={"title": "Witcher"})
        self.assertEqual(form.errors, {}) # If no error occur then form.error return empty dict

    def test_form_without_data(self):
        form = GoogleSearchForm(data={})
        self.assertEqual(form.errors, {"title":["This field is required."]})

    def test_form_one_author(self):
        form = GoogleSearchForm(data={"title":"Game of throne",
                                      "author":"R.R Marting"})
        self.assertEqual(form.errors, {})

    def test_form_multiple_authors(self):
        form = GoogleSearchForm(data={"title":"Game of throne",
                                      "author":["R.R Marting","J.K Rowling"]})
        self.assertEqual(form.errors, {})

class BookClassTest(TestCase):

    def setUp(self):
        pass