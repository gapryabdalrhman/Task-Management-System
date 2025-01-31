from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename="task")
# router.register('users', UserViewSet)

urlpatterns = [
    
    path('api/',include(router.urls)),
    # Django Template Views
    path("", task_list, name="task-list"),  
    path("tasks/form/", task_form, name="task-form"),  
    path('tasks/form/<int:task_id>/', task_form, name="task-form-edit"),  
]
