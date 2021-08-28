from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)



