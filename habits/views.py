from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwner


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Возвращает только привычки текущего пользователя.
        """
        return Habit.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        """
        Автоматически привязывает привычку к текущему пользователю.
        """
        serializer.save(user=self.request.user)


class PublicHabitViewSet(ReadOnlyModelViewSet):
    """
    Просмотр публичных привычек (доступно всем аутентифицированным пользователям).
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True).order_by('-created_at')
    pagination_class = None  # Убираем пагинацию для публичного списка
