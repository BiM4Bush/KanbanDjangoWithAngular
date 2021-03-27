from rest_framework import serializers
from Kanban.models import User, Board, Column, Note

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['name', 'board']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name', 'description', 'user', 'column']

class NoteMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name']
