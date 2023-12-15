from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Task, Image
from django import forms
from django.urls import reverse_lazy
from .forms import ImageForm
from django.http import Http404


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = Task.objects.all()

        # Search by title
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filter by creation date
        created = self.request.GET.get("created")
        if created:
            queryset = queryset.filter(created__date=created)

        # Filter by due date
        due_date = self.request.GET.get("due_date")
        if due_date:
            queryset = queryset.filter(due_date__date=due_date)

        # Filter by priority
        priority = self.request.GET.get("priority")
        if priority:
            queryset = queryset.filter(priority=priority)

        # Filter by completion status
        completed = self.request.GET.get("completed")
        if completed:
            completed = completed.lower() == "true"
            queryset = queryset.filter(completed=completed)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/new_task.html"
    fields = ["priority", "title", "description", "due_date", "completed"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task_edit.html"
    fields = ["priority", "title", "description", "due_date", "completed"]


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("task_list")


def new_image(request, pk):
    task = Task.objects.get(id=pk)
    if task.author != request.user:
        raise Http404
    if request.method != "POST":
        form = ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.task = task
            new_entry.save()
            return redirect("task_detail", pk=pk)

    context = {"task": task, "form": form}
    return render(request, "tasks/add_image.html", context)
