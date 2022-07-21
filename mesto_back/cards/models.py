from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    about = models.CharField(max_length=64)
    avatar = models.CharField(max_length=64)
    cohort = models.CharField(max_length=64)
    _id = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Card(models.Model):
    likes = models.ManyToManyField(User,
                                   through='Like')
    _id = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=64)
    owner = models.ForeignKey(
        User, related_name='cards', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    def __str__(self):
        return f'{self.name} {self.owner}'


class Like(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.card} {self.user}'
