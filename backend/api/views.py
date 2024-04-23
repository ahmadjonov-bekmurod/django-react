from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def main(request):
    return HttpResponse("<a href='/api'>API</a>")

@api_view(["GET"])
def todo_list(request):
    todos = ToDo.objects.all()
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)
