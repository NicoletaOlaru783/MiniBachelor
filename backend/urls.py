from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('accounts.urls')),
    path('', include('comments.urls')),
    path('', include('projects.urls')),
    path('', include('questions.urls')),
    path('admin/', admin.site.urls),
]
