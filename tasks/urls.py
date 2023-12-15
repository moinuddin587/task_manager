from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    new_image,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/new", TaskCreateView.as_view(), name="new_task"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="update_task"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="delete_task"),
    path("tasks/<int:pk>/image/", new_image, name="add_image"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
