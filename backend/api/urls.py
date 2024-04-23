from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.todo_list),
    path('', views.main)
]
