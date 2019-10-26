"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Supplemental


class SupplementalSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payment

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Supplemental
        url = serializers.HyperlinkedIdentityField(
            view_name='supplemental',
            lookup_field='id'
        )
        fields = ('id', 'url','title', 'text', 'language', 'supplemental_image', 'pinned', 'supplemental_type_id')


class Supplementals(ViewSet):

    def update(self, request, pk=None):
        """Handle PUT requests for a Supplemental

        Returns:
            Response -- Empty body with 204 status code
        """
        supplemental = Supplemental.objects.get(pk=pk)
        supplemental.profile_image = request.data["profile_image"]

        supplemental.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single task
        Methods:  GET
        Returns:
            Response -- JSON serialized task instance
        """
        try:
            supplemental = Supplemental.objects.get(pk=pk)
            serializer = SupplementalSerializer(supplemental, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    """Supplementals for codeProject"""

    def list(self, request):
        """Handle GET requests to Supplemental resource

        Returns:
            Response -- JSON serialized list of Supplementals
        """
        supplementals = Supplemental.objects.all()

        serializer = SupplementalSerializer(
            supplementals,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)