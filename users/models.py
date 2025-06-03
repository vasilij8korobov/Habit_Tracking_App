from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=50, **NULLABLE, verbose_name='Telegram Chat ID')
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_set',  # Уникальное имя
        related_query_name='user',
        verbose_name='Группы',
        help_text='Группы, к которым принадлежит пользователь'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Права доступа',
        blank=True,
        related_name='custom_user_set',  # Уникальное имя
        related_query_name='user',
        help_text='Конкретные права для этого пользователя'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
