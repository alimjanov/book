from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



class BookModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=1000)
    is_booked = models.ForeignKey(
        UserModel, verbose_name='user', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'books'


class CommentModel(models.Model):
    book = models.ForeignKey(
        BookModel, verbose_name='book', on_delete=models.SET_NULL, null=True
    )

    user = models.ForeignKey(
        UserModel, verbose_name='user', on_delete=models.SET_NULL, null=True, blank=True
    )

    commentary = models.TextField(max_length=1000)

