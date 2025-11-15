from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.pagination import PageNumberPagination


class TaskApiView(APIView):
    paginator = PageNumberPagination()

    def get_queryset(self, request):
        queryset = Task.objects.all()

        task_name = request.query_params.get("task_name", None)
        is_completed = request.query_params.get("is_completed", None) == "true"

        if task_name:
            queryset = queryset.filter(title__icontains=task_name)

        if is_completed:
            queryset = queryset.filter(is_completed=True)

        return queryset

    def get(self, request, pk=None):

        if pk == None:
            queryset = self.get_queryset(request)

            paginated_queryset = self.paginator.paginate_queryset(
                queryset, request)

            serializer = TaskSerializer(paginated_queryset, many=True)
            return self.paginator.get_paginated_response(serializer.data)
        else:
            try:
                task = Task.objects.get(id=pk)
            except Task.DoesNotExist:
                return Response({"message": "Task with the given id does not exixt"}, status=404)
            serializer = TaskSerializer(task)
        return Response({"data": serializer.data}, status=200)

    def post(self, request):
        data = request.data

        task_name = data.get("title", None)

        if not task_name:
            return Response({"message": "Title is required for creating task"}, status=400)

        serializer = TaskSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response({"message": f"New Task is created by id {task.id}"}, status=200)

    def put(self, request, pk=None):
        if not pk:
            return Response({"message": "Id is required for updating task"})

        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({"message": "Task with the given id does not exist"}, status=400)

        data = request.data

        serializer = TaskSerializer(task, data=data)

        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response({"message": "Task Updated"}, status=200)

    def patch(self, request, pk=None):
        if not pk:
            return Response({"message": "Id is required for updating task"}, status=400)

        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({"message": "Task with the given id does not exist"}, status=404)

        data = request.data

        serializer = TaskSerializer(task, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response({"message": "Task Updated"}, status=200)

    def delete(self, request, pk):
        if not pk:
            return Response({"message": "Id is required for updating task"}, status=400)

        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({"message": "Task with the given id does not exist"}, status=404)

        task.delete()

        return Response({"message": "Task with the given id is deleted"}, status=200)
