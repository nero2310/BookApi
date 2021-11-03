from django.urls import path

from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view),
    path('logout/', views.logout_user, name = 'logout_view'),
]
