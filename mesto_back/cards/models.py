# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser

from django.db import models


#
# User = get_user_model()


class User(AbstractUser):
    name = models.CharField(max_length=64, default="Жак-Ив-Кусто")
    about = models.CharField(max_length=64, default="Исследователь")
    avatar = models.CharField(max_length=64, blank=True, null=True)
    cohort = models.CharField(max_length=64, blank=True, default="cohort-45")
    # _id = models.AutoField(primary_key=True, blank=False)

    def __str__(self):
        return f'Имя юзера {self.name}'


class Card(models.Model):
    likes = models.ManyToManyField(User,
                                   through='Like')
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=150)
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

    class Meta:
        unique_together = ("card", "user")

    def __str__(self):
        return f'{self.card} {self.user}'
