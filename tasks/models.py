from django.db import models
from users.models import UserProfile


class Task(models.Model):
    name = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, related_name='user', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
