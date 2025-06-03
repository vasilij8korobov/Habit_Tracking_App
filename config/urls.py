from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from rest_framework.routers import DefaultRouter

from habits.views import HabitViewSet, PublicHabitViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')
router.register(r'public-habits', PublicHabitViewSet, basename='public-habits')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),

    # Документация
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema')),

]
