"""View module for handling requests about Collaborator Invites"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import CollaboratorInvite, Coder, ProjectCollaborator
from rest_framework.decorators import action



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
        fields = ('id', 'url', 'project','collaborator', 'owner_id','owner', 'message', 'accept')

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

    def update(self, request, pk=None):
        """Handle PUT requests for a Project

        Returns:
            Response -- Empty body with 204 status code
        """
        invite = CollaboratorInvite.objects.get(pk=pk)
        
        if request.data["accept"] == True:
            project_collaborator = ProjectCollaborator()
            project_collaborator.project = invite.project
            project_collaborator.collaborator = invite.collaborator
            project_collaborator.save()
            invite.delete()
        elif request.data["accept"] == False:
            invite.accept == False
            invite.delete()



        return Response({}, status=status.HTTP_204_NO_CONTENT)


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

    @action(methods=['get'], detail=False)
    def myinvites(self, request):

        invites = CollaboratorInvite.objects.all()
        current_user = Coder.objects.get(user=request.auth.user)
        invites = CollaboratorInvite.objects.filter(collaborator=current_user)

        serializer = CollaboratorInviteSerializer(
            invites, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def pendinginvites(self, request):

        invites = CollaboratorInvite.objects.all()
        current_user = Coder.objects.get(user=request.auth.user)
        invites = CollaboratorInvite.objects.filter(owner=current_user, accept=None)[:5]

        serializer = CollaboratorInviteSerializer(
            invites, many=True, context={'request': request})
        return Response(serializer.data)