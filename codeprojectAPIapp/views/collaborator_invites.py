"""View module for handling requests about Collaborator Invites"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import CollaboratorInvite, Coder


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
        fields = ('id', 'url', 'project','collaborator', 'owner', 'message', 'accept')

        depth = 2


class CollaboratorInvites(ViewSet):
    """Collaborator Invites for codeProject"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Task instance
        """
        invite = CollaboratorInvite()
        invite.project_id = request.data["project_id"]
        invite.collaborator_id = request.data["collaborator_id"]
        invite.owner = Coder.objects.get(user=request.auth.user)
        invite.message = request.data["message"]
        invite.save()

        serializer = CollaboratorInviteSerializer(invite, context={'request': request})

        return Response(serializer.data)

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