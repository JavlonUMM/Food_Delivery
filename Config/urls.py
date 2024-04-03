from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/jwt-login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/logout/', TokenBlacklistView.as_view(), name='token_black_list'),
    path('user/', include('user.urls')),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
