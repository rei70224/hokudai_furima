from django.conf.urls import url
from . import views
from django.urls import path
from .views import UserList

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('users/', UserList.as_view())
]
