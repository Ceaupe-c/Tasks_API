from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@csrf_exempt #Excepcion para funciones basadas en vistas
def tasks(request):
    '''
    List all task snippets
    '''
    if(request.method == 'GET'):
        tasks = Task.objects.all() #Obtencion de todas las tareas
        serializer = TaskSerializer(tasks, many=True) # Serializado de los datos de las tareas
        return JsonResponse(serializer.data,safe=False) #Retorno de un JsonResponse

    elif(request.method == 'POST'):
        data = JSONParser().parse(request) #Deserializacion de la data 
        serializer = TaskSerializer(data=data) #Instancia
        if(serializer.is_valid()): #Validacion de la informacion
            serializer.save() #Si es correcto, almacena en la DB
            return JsonResponse(serializer.data, status=201) #Si es correcto devuelve un Json con la info guardada
        return JsonResponse(serializer.errors, status=400) #Si es incorrecto devuelve un Json con la info del error

@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk) #Obtencion de la tarea validando el id
    except:
        return HttpResponse(status=404) 

    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
    elif(request.method == 'DELETE'):
            task.delete()
            return HttpResponse(status=204) 