from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from Kanban.serializers import *
from Kanban.models import *
# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwargs):
        notes = Note.objects.all()
        serializer = NoteMiniSerializer(notes, many=True)
        return Response(serializer.data)
