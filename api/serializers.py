from rest_framework import serializers
from .models import User
from .models import Item

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'is_active', 'is_staff', 'password']
        read_only_fields = ['id', 'is_staff', 'is_active']

# Use create_user to ensure password is hashed and other logic runs
# otherwise we have to set password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'user']
        read_only_fields = ['id', 'user']  