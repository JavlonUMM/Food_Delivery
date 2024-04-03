from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import RegistrationView
from .views import RegistrationAndLoginViewSet


router = DefaultRouter()
# router.register()

urlpatterns = [
    # path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration/', RegistrationAndLoginViewSet.as_view({"post": 'registration'})),
    path('registration/<str:user_type>/', RegistrationAndLoginViewSet.as_view({"post": 'registration'})),
    # path('login/', RegistrationAndLoginViewSet.as_view({"post": 'user_login'})),
]

