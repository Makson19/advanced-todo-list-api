from rest_framework import serializers
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'password', 'birthday', 'gender', 'created_at', 'updated_at')
        extra_kwargs = { 'password': { 'write_only': True } }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user
    

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
