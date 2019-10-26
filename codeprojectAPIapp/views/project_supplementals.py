"""View module for handling requests about project Supplementals"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import ProjectSupplemental


class ProjectSupplementalSerializer(serializers.HyperlinkedModelSerializer):

    """JSON serializer for project Supplementals

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = ProjectSupplemental
        url = serializers.HyperlinkedIdentityField(
            view_name='project_supplemental',
            lookup_field='id'
        )
        fields = ('id', 'url', 'project_id', 'supplemental_id')


class ProjectSupplementals(ViewSet):
    """ProjectSupplementals for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project supplementals

        Returns:
            Response -- JSON serialized project supplemental instance
        """
        try:
            project_supplemental = ProjectSupplemental.objects.get(pk=pk)
            serializer = ProjectSupplementalSerializer(project_supplemental, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to project supplementals resource

        Returns:
            Response -- JSON serialized list of project supplementals
        """
        project_supplemental = ProjectSupplemental.objects.all()
        serializer = ProjectSupplementalSerializer(
            project_supplemental,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)