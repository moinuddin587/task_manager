from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Task
from django import forms
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/new_task.html"
    fields = ["priority", "title", "description", "due_date", "completed", "photos"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "update_task.html"
    fields = ["title", "description", "due_date", "priority", "completed"]


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete_task.html"
    success_url = reverse_lazy("home")
