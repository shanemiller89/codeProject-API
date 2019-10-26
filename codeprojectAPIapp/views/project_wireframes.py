"""View module for handling requests about project Wireframes"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import ProjectWireframe


class ProjectWireframeSerializer(serializers.HyperlinkedModelSerializer):

    """JSON serializer for project Wireframes

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = ProjectWireframe
        url = serializers.HyperlinkedIdentityField(
            view_name='project_wireframe',
            lookup_field='id'
        )
        fields = ('id', 'url', 'project_id', 'wireframe_id')


class ProjectWireframes(ViewSet):
    """ProjectWireframes for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project Wireframes

        Returns:
            Response -- JSON serialized project Wireframe instance
        """
        try:
            project_wireframe = ProjectWireframe.objects.get(pk=pk)
            serializer = ProjectWireframeSerializer(project_wireframe, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to project Wireframes resource

        Returns:
            Response -- JSON serialized list of project Wireframes
        """
        project_wireframe = ProjectWireframe.objects.all()
        serializer = ProjectWireframeSerializer(
            project_wireframe,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)