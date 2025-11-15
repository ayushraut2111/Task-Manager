from django.db import models
from task_manager.models import BaseModel


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
