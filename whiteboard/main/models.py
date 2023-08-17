

# Create your models here.
# whiteboard_app/models.py

from django.db import models

class Whiteboard(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class DrawingAction(models.Model):
    whiteboard = models.ForeignKey(Whiteboard, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
