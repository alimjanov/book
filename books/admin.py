from django.contrib import admin

from books.models import BookModel, UserModel, CommentModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']
    list_filter = ['title']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'commentary']

