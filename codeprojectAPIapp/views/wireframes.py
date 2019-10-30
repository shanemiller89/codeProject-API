"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Wireframe, ProjectWireframe


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
        fields = ('id', 'url', 'wireframe_title', 'wireframe_image')


class Wireframes(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Project instance
        """
        wireframe = Wireframe()
        wireframe.wireframe_image = request.data["wireframe_image"]
        wireframe.save()

        project_wireframe = ProjectWireframe()
        project_wireframe.project_id = request.data["project_id"]
        project_wireframe.wireframe = wireframe
        project_wireframe.save()

        serializer = WireframeSerializer(wireframe, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a Wireframe

        Returns:
            Response -- Empty body with 204 status code
        """
        wireframe = Wireframe.objects.get(pk=pk)
        wireframe.wireframe_title = request.data["wireframe_title"]

        wireframe.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single wireframe

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            wireframe = Wireframe.objects.get(pk=pk)
            wireframe.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Wireframe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
