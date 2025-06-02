from rest_framework.exceptions import ValidationError


def validate_habit_fields(data):
    # Нельзя одновременно указать вознаграждение и связанную привычку
    if data.get('related_habit') and data.get('reward'):
        raise ValidationError("Выберите что-то одно: вознаграждение или связанную привычку.")

    # Приятная привычка не может иметь вознаграждения или связанной привычки
    if data.get('is_pleasant'):
        if data.get('related_habit') or data.get('reward'):
            raise ValidationError("Приятная привычка не может иметь вознаграждения или связанной привычки.")

    # Связанная привычка должна быть приятной
    if related_habit := data.get('related_habit'):
        if not related_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")
