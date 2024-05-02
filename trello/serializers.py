from rest_framework import serializers
from.models import User, Column, Card

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'order']

class CardSerializer(serializers.ModelSerializer):
    column = serializers.PrimaryKeyRelatedField(queryset=Column.objects.all())

    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'column', 'order']

    def validate_title(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Title should only contain alphabets.')
        return value

    def validate_description(self, value):
        if len(value) < 25:
            raise serializers.ValidationError('Description should be at least 25 characters.')
        return value