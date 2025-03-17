from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'completed')
    search_fields = ('title', 'description')
    list_filter = ('completed',)
    ordering = ('created_at',)