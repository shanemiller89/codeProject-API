"""View module for handling requests about Coders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Technology, ProjectTechnology


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

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Project instance
        """

        supplemental_technology = Technology()
        supplemental_technology.technology_type_id = 2
        supplemental_technology.technology = request.data["technology"]
        supplemental_technology.save()
        supplemental_project_technology = ProjectTechnology()
        supplemental_project_technology.project_id = request.data["project_id"]
        supplemental_project_technology.technology = supplemental_technology
        supplemental_project_technology.save()


        serializer = TechnologySerializer(supplemental_technology, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a Technology

        Returns:
            Response -- Empty body with 204 status code
        """
        technology = Technology.objects.get(pk=pk)
        technology.technology = request.data["technology"]

        technology.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single project

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            technology = Technology.objects.get(pk=pk)
            technology.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Project.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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