from django.urls import path

from .views import AuthorDetail

urlpatterns = [
    path('detail/<slug:slug>/', AuthorDetail.as_view()),
]