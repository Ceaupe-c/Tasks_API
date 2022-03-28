from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.tasks),
    path('task/<int:pk>', views.task_detail),
]
