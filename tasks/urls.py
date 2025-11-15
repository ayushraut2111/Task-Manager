from django.urls import path
from tasks.views import TaskApiView

urlpatterns = [
    path('task/', TaskApiView.as_view(), name='task-list'),
    path('task/<uuid:pk>/', TaskApiView.as_view(), name='task-detail'),
]
