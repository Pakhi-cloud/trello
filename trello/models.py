from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class Column(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')
    order = models.IntegerField(default=0)