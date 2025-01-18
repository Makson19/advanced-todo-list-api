from django.contrib import admin
from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birthday', 'gender', 'created_at', 'updated_at', 'last_login')
    search_fields = ['name']
