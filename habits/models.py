from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from config.settings import NULLABLE
from users.models import User


class Habit(models.Model):
    PERIOD_CHOICES = [
        (1, 'Ежедневно'),
        (2, 'Через день'),
        (7, 'Еженедельно'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', verbose_name='Пользователь')
    place = models.CharField(max_length=255, verbose_name='Место')
    time = models.TimeField(verbose_name='Время выполнения')
    action = models.TextField(verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        choices=PERIOD_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        verbose_name='Периодичность'
    )
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Вознаграждение')
    time_to_complete = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        default=60,
        verbose_name='Время на выполнение'
    )
    is_public = models.BooleanField(default=False, verbose_name='Опубликовать')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.user}: {self.action} в {self.time}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
