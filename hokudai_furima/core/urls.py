from django.conf.urls import url
from . import views
from django.urls import path
from .views import UserList, current_user

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('users/', UserList.as_view()),
    path('current_user/', current_user),
]
