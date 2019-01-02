from django.urls import path
from . import views

app_name = "watchlist"

urlpatterns = [
    path('', views.show_watch_list, name='show_watch_list'),
    path('add', views.add_watch_list, name='add_watch_list'),
]
