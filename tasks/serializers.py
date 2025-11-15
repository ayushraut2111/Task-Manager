from rest_framework.serializers import ModelSerializer
from tasks.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields=['id','title','is_completed','description']