from django.db import models
from habits.models import Habit
from users.models import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='notifications')
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name='Привычка')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    status = models.BooleanField(default=False, verbose_name='Статус отправки')

    def __str__(self):
        return f"Уведомление для {self.user} о {self.habit}"

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        ordering = ['-sent_at']
