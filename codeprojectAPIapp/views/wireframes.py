"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Wireframe


class WireframeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payment

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Wireframe
        url = serializers.HyperlinkedIdentityField(
            view_name='wireframe_image',
            lookup_field='id'
        )
        fields = ('id', 'url', 'wireframe_image')


class Wireframes(ViewSet):

    def update(self, request, pk=None):
        """Handle PUT requests for a Wireframe

        Returns:
            Response -- Empty body with 204 status code
        """
        wireframe = Wireframe.objects.get(pk=pk)
        wireframe.profile_image = request.data["profile_image"]

        wireframe.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single wireframe
        Methods:  GET
        Returns:
            Response -- JSON serialized wireframe instance
        """
        try:
            wireframe = Wireframe.objects.get(pk=pk)
            serializer = WireframeSerializer(
                wireframe, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    """Wireframes for codeProject"""

    def list(self, request):
        """Handle GET requests to Wireframe resource

        Returns:
            Response -- JSON serialized list of Wireframes
        """
        wireframes = Wireframe.objects.all()

        serializer = WireframeSerializer(
            wireframes,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
