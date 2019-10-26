"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Technology 


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payment

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Technology
        url = serializers.HyperlinkedIdentityField(
            view_name='technology',
            lookup_field='id'
        )
        fields = ('id', 'url', 'technology', 'technology_type_id')


class Technologies(ViewSet):

    def update(self, request, pk=None):
        """Handle PUT requests for a Technology

        Returns:
            Response -- Empty body with 204 status code
        """
        technology = Technology.objects.get(pk=pk)
        technology.profile_image = request.data["profile_image"]

        technology.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single technology
        Methods:  GET
        Returns:
            Response -- JSON serialized technology instance
        """
        try:
            technology = Technology.objects.get(pk=pk)
            serializer = TechnologySerializer(technology, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    """Technologies for codeProject"""

    def list(self, request):
        """Handle GET requests to Technology resource

        Returns:
            Response -- JSON serialized list of Technologies
        """
        technologies = Technology.objects.all()

        serializer = TechnologySerializer(
            technologies,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)