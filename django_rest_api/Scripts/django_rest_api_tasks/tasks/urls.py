from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.tasks), #Traer tareas
    path('tasks/<int:pk>', views.task_detail), #Actualizar y eliminar tareas, id dinamico
]
