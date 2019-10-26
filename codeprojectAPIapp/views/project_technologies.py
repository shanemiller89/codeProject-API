"""View module for handling requests about project Technologies"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import ProjectTechnology


class ProjectTechnologySerializer(serializers.HyperlinkedModelSerializer):

    """JSON serializer for project Technologies

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = ProjectTechnology
        url = serializers.HyperlinkedIdentityField(
            view_name='project_technology',
            lookup_field='id'
        )
        fields = ('id', 'url', 'project_id', 'technology_id')


class ProjectTechnologies(ViewSet):
    """ProjectTechnologies for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project technologies

        Returns:
            Response -- JSON serialized project technology instance
        """
        try:
            project_technology = ProjectTechnology.objects.get(pk=pk)
            serializer = ProjectTechnologySerializer(project_technology, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to project technologies resource

        Returns:
            Response -- JSON serialized list of project technologies
        """
        project_technology = ProjectTechnology.objects.all()
        serializer = ProjectTechnologySerializer(
            project_technology,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)