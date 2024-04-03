from rest_framework import serializers
from user.models import User

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(required=True, min_length=8)
    password2 = serializers.CharField(required=True, min_length=8)

    class Meta:
        fields = ['email', 'password1', 'password2']

    def validate_email(self, value):
        if User.filter(email=value).exists():
            raise serializers.ValidationError("This email already exist")
        return value

    def validate(self, attrs):
        password1 = attrs['password1']
        password2 = attrs['password2']
        if password1 != password2:
            raise serializers.ValidationError("This passwords wrong")
        return attrs

