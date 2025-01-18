from django.urls import path
from tasks.views import TaskCreateListView, TaskRetrieveUpdateDestroyView


urlpatterns = [
    path('tasks', TaskCreateListView.as_view(), name='task-create-list'),
    path('tasks/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-details-view'),
]
