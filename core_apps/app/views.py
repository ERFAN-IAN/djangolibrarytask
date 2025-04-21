from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book
from django.db.models import Q

# Create your views here.


class AuthorListView(ListView):
    model = Author
    template_name = "app/home.html"
    context_object_name = "authors"

    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     if query:
    #         return Author.objects.filter(
    #             Q(first_name__icontains=query)
    #             | Q(last_name__icontains=query)
    #             | Q(national_id__icontains=query)
    #         )
    #     return Author.objects.all()


class AuthorCreateView(CreateView):
    model = Author
    fields = ["first_name", "last_name", "age", "national_id"]
    template_name = "app/add_author_form.html"
    success_url = reverse_lazy("home")
