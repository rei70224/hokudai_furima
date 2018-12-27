from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('thirdparty/rakuten/book', views.get_price_from_isbn_rakuten, name='rakuten_isbn'),
]
