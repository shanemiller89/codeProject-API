"""View module for handling requests about technology types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import TechnologyType


class TechnologyTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for technology types

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = TechnologyType
        url = serializers.HyperlinkedIdentityField(
            view_name='technologytype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'type')


class TechnologyTypes(ViewSet):
    """Technology Types for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for technology type

        Returns:
            Response -- JSON serialized technology type instance
        """
        try:
            technology_type = TechnologyType.objects.get(pk=pk)
            serializer = TechnologyTypeSerializer(technology_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to technology types resource

        Returns:
            Response -- JSON serialized list of technology types
        """
        technology_types = TechnologyType.objects.all()
        serializer = TechnologyTypeSerializer(
            technology_types,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)