from .models import UserModel
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        # إنشاء المستخدم باستخدام create_user لضمان تشفير كلمة المرور
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user