from django.db import models


class New(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name.title()}'
