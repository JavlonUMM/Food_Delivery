from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import User
from .serializers import RegistrationSerializer


class RegistrationAndLoginViewSet(viewsets.ViewSet):

    def registration(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if 'user_type' in self.kwargs:
                user_type = self.kwargs['user_type']
            else:
                user_type = 'customer'
            email = serializer.validated_data['email']
            password = serializer._validated_data['password']
            user = User.objects.create(email=email, user_type=user_type)
            user.set_password(password)
            user.save()
            return Response({"Message": "User created successfully"}, status.HTTP_201_CREATED)