"""View module for handling requests about task types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import TaskType


class TaskTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for task types

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = TaskType
        url = serializers.HyperlinkedIdentityField(
            view_name='tasktype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'type')


class TaskTypes(ViewSet):
    """Task Types for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for task type

        Returns:
            Response -- JSON serialized task type instance
        """
        try:
            task_type = TaskType.objects.get(pk=pk)
            serializer = TaskTypeSerializer(task_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to task types resource

        Returns:
            Response -- JSON serialized list of task types
        """
        task_types = TaskType.objects.all()
        serializer = TaskTypeSerializer(
            task_types,
            many=True, 
            context={'request': request}
        )
        return Response(serializer.data)