from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Title'
    )
    text = models.TextField(
        verbose_name='Text'
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Author'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )

    def __str__(self):
        return self.title
