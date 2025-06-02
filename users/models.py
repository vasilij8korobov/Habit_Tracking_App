from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=50, **NULLABLE, verbose_name='Telegram Chat ID')
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Уникальное имя
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Уникальное имя
        related_query_name='user',
    )

    def __str__(self):
        return self.username
