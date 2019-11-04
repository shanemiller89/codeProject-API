"""View module for handling requests about project collaborators"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import ProjectCollaborator


class ProjectCollaboratorSerializer(serializers.HyperlinkedModelSerializer):

    """JSON serializer for project collaborators

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = ProjectCollaborator
        url = serializers.HyperlinkedIdentityField(
            view_name='project_collaborator',
            lookup_field='id'
        )
        fields = ('id', 'url', 'project_id', 'collaborator_id')


class ProjectCollaborators(ViewSet):

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single collaborator

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            project_collaborator = ProjectCollaborator.objects.get(pk=pk)
            project_collaborator.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Task.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    """ProjectCollaborators for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single archives

        Returns:
            Response -- JSON serialized project collaborator instance
        """
        try:
            project_collaborator = ProjectCollaborator.objects.get(pk=pk)
            serializer = ProjectCollaboratorSerializer(project_collaborator, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to project collaborators resource

        Returns:
            Response -- JSON serialized list of project collaborators
        """
        project_collaborator = ProjectCollaborator.objects.all()
        serializer = ProjectCollaboratorSerializer(
            project_collaborator,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)