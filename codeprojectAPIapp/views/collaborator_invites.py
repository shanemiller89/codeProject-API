"""View module for handling requests about Collaborator Invites"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import CollaboratorInvite


class CollaboratorInviteSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Collaborator Invite

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = CollaboratorInvite
        url = serializers.HyperlinkedIdentityField(
            view_name='collaboratorinvite',
            lookup_field='id'
        )
        fields = ('id', 'url', 'collaborator', 'owner', 'message', 'accept')


class CollaboratorInvites(ViewSet):
    """Collaborator Invites for codeProject"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for Collaborator Invites

        Returns:
            Response -- JSON serialized Collaborator Invites instance
        """
        try:
            collaborator_invite = CollaboratorInvite.objects.get(pk=pk)
            serializer = CollaboratorInviteSerializer(collaborator_invite, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to collaborator invite resource

        Returns:
            Response -- JSON serialized list of collaborator invites
        """
        collaborator_invites = CollaboratorInvite.objects.all()
        serializer = CollaboratorInviteSerializer(
            collaborator_invites,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)