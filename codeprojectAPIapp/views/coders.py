"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Coder
from rest_framework.decorators import action


class CoderSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for coder

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Coder
        url = serializers.HyperlinkedIdentityField(
            view_name='coder',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'primary_language', 'github', 'profile_image')
        depth = 1


class Coders(ViewSet):

    def update(self, request, pk=None):
        """Handle PUT requests for a coder

        Returns:
            Response -- Empty body with 204 status code
        """
        coder = Coder.objects.get(pk=pk)
        coder.profile_image = request.data["profile_image"]

        coder.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single coder
        Methods:  GET
        Returns:
            Response -- JSON serialized coder instance
        """
        try:
            coder = Coder.objects.get(pk=pk)
            serializer = CoderSerializer(coder, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    """Coders for codeProject"""

    def list(self, request):
        """Handle GET requests to coder resource

        Returns:
            Response -- JSON serialized list of coders
        """
        coders = Coder.objects.all()

                #filter by location id
        users = self.request.query_params.get('users', None)

        if users == "":
            coders = Coder.objects.all()
        elif users is not None:
            coders = Coder.objects.filter(user__username__contains = users.lower())

        serializer = CoderSerializer(
            coders,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


    @action(methods=['get'], detail=False)
    def profile(self, request):

        current_user = Coder.objects.get(user=request.auth.user)

        serializer = CoderSerializer(current_user, many=False, context={'request': request})
        return Response(serializer.data)