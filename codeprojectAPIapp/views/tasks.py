"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Task, ProjectTask


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payment

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Task
        url = serializers.HyperlinkedIdentityField(
            view_name='task',
            lookup_field='id'
        )
        fields = ('id', 'url', 'task', 'task_type_id')


class Tasks(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Task instance
        """
        task = Task()
        task.task = request.data["task"]
        task.task_type_id = 1
        task.save()

        project_task = ProjectTask()
        project_task.project_id = request.data["project_id"]
        project_task.task = task
        project_task.save()

        serializer = TaskSerializer(task, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a Task

        Returns:
            Response -- Empty body with 204 status code
        """
        task = Task.objects.get(pk=pk)
        task.profile_image = request.data["profile_image"]

        task.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single task
        Methods:  GET
        Returns:
            Response -- JSON serialized task instance
        """
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    """Tasks for codeProject"""

    def list(self, request):
        """Handle GET requests to Task resource

        Returns:
            Response -- JSON serialized list of Tasks
        """
        tasks = Task.objects.all()

        serializer = TaskSerializer(
            tasks,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)