from rest_framework import serializers
from .models import Habit
from .validators import validate_habit_fields


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(
        help_text="Время на выполнение в секундах (макс. 120)"
    )

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        validate_habit_fields(data)
        return data
