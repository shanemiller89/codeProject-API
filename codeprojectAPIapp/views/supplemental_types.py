"""View module for handling requests about supplemental types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import SupplementalType


class SupplementalTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for supplemental types

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = SupplementalType
        url = serializers.HyperlinkedIdentityField(
            view_name='supplementaltype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'type')


class SupplementalTypes(ViewSet):
    """Supplemental Types for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for task type

        Returns:
            Response -- JSON serialized task type instance
        """
        try:
            supplemental_type = SupplementalType.objects.get(pk=pk)
            serializer = SupplementalTypeSerializer(supplemental_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to supplemental types resource

        Returns:
            Response -- JSON serialized list of supplemental types
        """
        supplemental_types = SupplementalType.objects.all()
        serializer = SupplementalTypeSerializer(
            supplemental_types,
            many=True, 
            context={'request': request}
        )
        return Response(serializer.data)