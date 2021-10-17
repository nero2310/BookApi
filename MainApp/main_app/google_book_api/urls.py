from django.urls import path

from .views import BookSearch, LibraryDetail, BookDetailView

urlpatterns = [
    path('search/', BookSearch.as_view()),
    path('library/', LibraryDetail.as_view()),
    path('<slug:slug>', BookDetailView.as_view()),
]
