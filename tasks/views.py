from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task
from .serializers import TaskSerializer,UserSerializer

#separation of concerns between API and template views

# REST API Views (JWT Protected)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint for managing tasks (JWT Authentication Required)"""
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
     
    def get_queryset(self):
        """Ensure users can only access their own tasks"""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically assign the logged-in user to the task"""
        serializer.save(user=self.request.user)

# Django Template Views (Login Required) 

@login_required
def task_list(request):
    """View to display all tasks for the logged-in user (JWT/Login Required)"""
    tasks = Task.objects.filter(user=request.user)
    return render(request, "task_list.html", {"tasks": tasks})


@login_required
def task_form(request, task_id=None):
    """View to create or edit a task (JWT/Login Required)"""
    task = get_object_or_404(Task, id=task_id, user=request.user) if task_id else None

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        completed = request.POST.get("completed") == "on"

        if task:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
        else:
            Task.objects.create(title=title, description=description, completed=completed, user=request.user)

        return redirect("task-list")

    return render(request, "task_form.html", {"task": task})
