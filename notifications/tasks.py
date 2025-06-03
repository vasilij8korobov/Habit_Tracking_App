from celery import shared_task
import requests
from django.conf import settings
from habits.models import Habit
from datetime import datetime


@shared_task
def send_telegram_reminder():
    now = datetime.now().time()
    habits = Habit.objects.filter(time__hour=now.hour, time__minute=now.minute)

    for habit in habits:
        text = f"⏰ Напоминание: {habit.action} в {habit.time} ({habit.place})"
        requests.post(
            f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage",
            data={"chat_id": habit.user.telegram_chat_id, "text": text}
        )
