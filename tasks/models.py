from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = "H", "High"
        MEDIUM = "M", "Medium"
        LOW = "L", "Low"

    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=1, choices=Priority.choices)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField("Image", related_name="task_photos", blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="authors/%Y/%m/%d/", blank=True)
