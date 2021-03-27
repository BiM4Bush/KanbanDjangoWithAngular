from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=45)

class User(models.Model):
    name = models.CharField(max_length=500)

class Column(models.Model):
    name = models.CharField(max_length=500, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Note(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)

