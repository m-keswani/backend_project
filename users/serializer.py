from rest_framework import serializers
from .models import *

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'password']

    def create(self, validated_data):
        user = User(
            nickname=validated_data['nickname'],
            username=validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class SleepAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAssessment
        fields = ['user', 'question', 'answer']
