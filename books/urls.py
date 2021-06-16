from django.urls import path
from books.views import HomeView, BookDetailView

app_name = 'books'


urlpatterns = [
    path('', HomeView.as_view(), name='book'),
    path('about', BookDetailView.as_view(), name='detail'),
]