from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskRegister(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
