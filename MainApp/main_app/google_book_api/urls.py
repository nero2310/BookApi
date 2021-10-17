from django.urls import path

from .views import BookDetail, LibraryDetail

urlpatterns = [
    path('search/',BookDetail.as_view()),
    path('library/',LibraryDetail.as_view())
]