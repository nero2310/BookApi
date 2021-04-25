from django.urls import path

from views import BookDetail

urlpatterns = [
    path('detail/',BookDetail.as_view()),
]