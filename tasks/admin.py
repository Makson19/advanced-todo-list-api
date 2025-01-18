from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'completed', 'user', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ('completed', 'user')

