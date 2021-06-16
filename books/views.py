from django.shortcuts import render
from django.views.generic import DetailView
from books.models import BookModel


class HomeView(DetailView):
    template_name = 'index.html'
    queryset = BookModel.objects.order_by('-pk')


class BookDetailView(DetailView):
    template_name = 'detail.html'
    queryset = BookModel.objects.order_by('-pk')