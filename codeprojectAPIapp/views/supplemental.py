"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Supplemental, ProjectSupplemental
from rest_framework.decorators import action



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

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Task instance
        """

        if request.data["supplemental_type_id"] == 1:
            supplemental = Supplemental()
            supplemental.title = request.data["title"]
            supplemental.text = request.data["text"]
            supplemental.supplemental_type_id = 1
            supplemental.save()

            project_supplemental = ProjectSupplemental()
            project_supplemental.project_id = request.data["project_id"]
            project_supplemental.supplemental = supplemental
            project_supplemental.save()

        if request.data["supplemental_type_id"] == 2:
            supplemental = Supplemental()
            supplemental.title = request.data["title"]
            supplemental.text = request.data["text"]
            supplemental.language = request.data["language"]
            supplemental.supplemental_type_id = 2
            supplemental.save()

            project_supplemental = ProjectSupplemental()
            project_supplemental.project_id = request.data["project_id"]
            project_supplemental.supplemental = supplemental
            project_supplemental.save()

        if request.data["supplemental_type_id"] == 3:
            supplemental = Supplemental()
            supplemental.title = request.data["title"]
            supplemental.supplemental_image = request.data["supplemental_image"]
            supplemental.supplemental_type_id = 3
            supplemental.save()

            project_supplemental = ProjectSupplemental()
            project_supplemental.project_id = request.data["project_id"]
            project_supplemental.supplemental = supplemental
            project_supplemental.save()

        serializer = SupplementalSerializer(supplemental, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single project

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            supplemental = Supplemental.objects.get(pk=pk)
            supplemental.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Supplemental.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

    @action(methods=['put'], detail=False)
    def updatenote(self, request):
        """Handle PUT requests for Project Overview
        Returns:
            Response -- Empty body with 204 status code
        """
        supplemental = Supplemental.objects.get(pk=request.data["supplemental_id"])
        supplemental.title = request.data["title"]
        supplemental.text = request.data["text"]
        supplemental.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['put'], detail=False)
    def updatecode(self, request):
        """Handle PUT requests for Project Overview
        Returns:
            Response -- Empty body with 204 status code
        """
        supplemental = Supplemental.objects.get(pk=request.data["supplemental_id"])
        supplemental.title = request.data["title"]
        supplemental.text = request.data["text"]
        supplemental.language = request.data["language"]

        supplemental.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)