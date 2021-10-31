from django.urls import path

from .views import book_search, book_search_results, book_detail_view, LibraryDetail

urlpatterns = [
    path('search', book_search),
    path('search-results/<str:title>', book_search_results, name = 'search_results'),
    path('search-results/<str:title>/<str:author>', book_search_results, name = 'search_results'),
    # path('serarch-results/<str:title>', BookSearch.as_view()),
    path('library', LibraryDetail.as_view()),
    path('<slug:slug>', book_detail_view),
]
