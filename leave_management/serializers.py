from rest_framework import serializers
from .models import User, Leave


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = [
            'userId',
            'firstName',
            'lastName',
            'email',
            'designation',
            'dateOfBirth',
            'supervisor',
            'password'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for key in validated_data:
            setattr(instance, key, validated_data[key])
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
class LeaveSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Leave
        fields = [
            'leaveId',
            'from',
            'to',
            'type',
            'reason',
            'emergencyContact',
            'userId'
        ]