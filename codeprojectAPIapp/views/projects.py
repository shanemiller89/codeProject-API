"""View module for handling requests about Projects"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Project, Coder
from rest_framework.decorators import action


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Projects

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Project
        url = serializers.HyperlinkedIdentityField(
            view_name='project',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'repo', 'overview', 'project_image', 'erd_image', 'private', 'technologies', 'wireframes', 'tasks', 'supplementals', 'collaborators', 'owner')
        depth = 1


class Projects(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project
        Methods:  GET
        Returns:
            Response -- JSON serialized project instance
        """
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    """Projects for codeProject"""

    def list(self, request):
        """Handle GET requests to Project resource

        Returns:
            Response -- JSON serialized list of Projects
        """
        projects = Project.objects.all()

        serializer = ProjectSerializer(
            projects,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


    @action(methods=['get'], detail=False)
    def owner(self, request):

        current_user = Coder.objects.get(user=request.auth.user)
        projects = Project.objects.get(owner=current_user)

        serializer = ProjectSerializer(projects, many=False, context={'request': request})
        return Response(serializer.data)