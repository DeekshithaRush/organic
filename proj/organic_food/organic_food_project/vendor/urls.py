# vendor/urls.py
from django.urls import path
from . import views

app_name = 'vendor'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('add_product/', views.add_product_view, name='add_product'),
    # Define more URL patterns as needed
]
