"""View module for handling requests about project Tasks"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import ProjectTask


class ProjectTaskSerializer(serializers.HyperlinkedModelSerializer):

    """JSON serializer for project Tasks

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = ProjectTask
        url = serializers.HyperlinkedIdentityField(
            view_name='project_task',
            lookup_field='id'
        )
        fields = ('id', 'url', 'project_id', 'task_id')


class ProjectTasks(ViewSet):
    """ProjectTasks for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project Tasks

        Returns:
            Response -- JSON serialized project Task instance
        """
        try:
            project_task = ProjectTask.objects.get(pk=pk)
            serializer = ProjectTaskSerializer(project_task, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to project Tasks resource

        Returns:
            Response -- JSON serialized list of project Tasks
        """
        project_task = ProjectTask.objects.all()
        serializer = ProjectTaskSerializer(
            project_task,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)