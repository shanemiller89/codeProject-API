"""View module for handling requests about project Tasks"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import ProjectTask, Coder
from .tasks import TaskSerializer


class ProjectTaskSerializer(serializers.HyperlinkedModelSerializer):

    """JSON serializer for project Tasks

    Arguments:
        serializers.HyperlinkedModelSerializer

    """

    task = TaskSerializer(many=False)
    class Meta:
        model = ProjectTask
        url = serializers.HyperlinkedIdentityField(
            view_name='project_task',
            lookup_field='id'
        )
        fields = ('id', 'url', 'project', 'task')

        depth = 1


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

        project_task= ProjectTask.objects.all()
        current_user = Coder.objects.get(user=request.auth.user)
        project_task = ProjectTask.objects.filter(project__owner=current_user, task__task_type_id=1)[:5]

        serializer = ProjectTaskSerializer(
            project_task,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)