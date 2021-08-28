from django.urls import path
from .views import TaskAPIView, TaskDetailAPIView, TaskSetFinishedAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task_list_url'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task_detail_url'),
    path('tasks/<int:id>/finished/', TaskSetFinishedAPIView.as_view(), name = 'task_set_finished_url')
]
