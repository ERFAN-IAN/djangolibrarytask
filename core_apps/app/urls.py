from django.contrib import admin
from django.urls import path, include
from .views import AuthorListView, AuthorCreateView

urlpatterns = [
    path("", AuthorListView.as_view(), name="home"),
    path("add_author", AuthorCreateView.as_view(), name="add_author"),
]
