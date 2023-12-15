from django.contrib import admin
from .models import Task, Image


class ImageItems(admin.TabularInline):
    model = Image


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created", "updated", "priority", "completed"]
    ordering = ["priority"]
    inlines = [ImageItems]
