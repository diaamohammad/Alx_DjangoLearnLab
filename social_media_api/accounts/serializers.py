from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # تعريف حقل كلمة المرور كـ write_only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # إنشاء المستخدم باستخدام create_user لضمان تشفير كلمة المرور
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # توليد توكن مرتبط بالمستخدم
        Token.objects.create(user=user)

        return user
