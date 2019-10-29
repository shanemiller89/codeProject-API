"""View module for handling requests about Projects"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from codeprojectAPIapp.models import Project, Coder, Technology, ProjectTechnology
from rest_framework.decorators import action


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Projects

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Project
        url = serializers.HyperlinkedIdentityField(
            view_name='project',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'repo', 'overview', 'project_image', 'erd_image', 'private',
                  'technologies', 'wireframes', 'tasks', 'supplementals', 'collaborators', 'owner')
        depth = 1


class Projects(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Project instance
        """
        project = Project()
        project.title = request.data["title"]
        project.repo = request.data["repo"]
        project.overview = request.data["overview"]
        project.private = request.data["private"]
        project.project_image = request.data["project_image"]
        project.owner = Coder.objects.get(user=request.auth.user)
        project.save()

        primary_technology = Technology()
        primary_technology.technology_type_id = 1
        primary_technology.technology = request.data["primary_technology"]
        primary_technology.save()

        primary_project_technology = ProjectTechnology()
        primary_project_technology.project = project
        primary_project_technology.technology = primary_technology
        primary_project_technology.save()

        supplemental_technologies = request.data["supplemental_technologies"]

        for technology in supplemental_technologies:

            supplemental_technology = Technology()
            supplemental_technology.technology_type_id = 2
            supplemental_technology.technology = technology
            supplemental_technology.save()
            supplemental_project_technology = ProjectTechnology()
            supplemental_project_technology.project = project
            supplemental_project_technology.technology = supplemental_technology
            supplemental_project_technology.save()


        serializer = ProjectSerializer(project, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single project

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            project = Project.objects.get(pk=pk)
            project.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Project.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single project
        Methods:  GET
        Returns:
            Response -- JSON serialized project instance
        """
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(
                project, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    """Projects for codeProject"""

    def list(self, request):
        """Handle GET requests to Project resource

        Returns:
            Response -- JSON serialized list of Projects
        """
        projects = Project.objects.all()

        serializer = ProjectSerializer(
            projects,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def owner(self, request):

        projects = Project.objects.all()
        current_user = Coder.objects.get(user=request.auth.user)
        projects = Project.objects.filter(owner=current_user)

        serializer = ProjectSerializer(
            projects, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['put'], detail=False)
    def overview(self, request):
        """Handle PUT requests for Project Overview
        Returns:
            Response -- Empty body with 204 status code
        """
        project = Project.objects.get(pk=request.data["id"])
        project.overview = request.data["overview"]
        project.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['put'], detail=False)
    def erd(self, request):
        """Handle PUT requests for Project Overview
        Returns:
            Response -- Empty body with 204 status code
        """
        project = Project.objects.get(pk=request.data["id"])
        project.erd_image = request.data["erd_image"]
        project.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

