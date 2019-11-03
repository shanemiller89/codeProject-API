"""codeprojectAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from codeprojectAPIapp.views import register_user, login_user, Coders, UserViewSet, TechnologyTypes, TaskTypes, Tasks, SupplementalTypes, Technologies
from codeprojectAPIapp.views import Wireframes, Supplementals, ProjectCollaborators, ProjectSupplementals, ProjectTasks
from codeprojectAPIapp.views import ProjectTechnologies, ProjectWireframes, Projects, CollaboratorInvites

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'supplementals', Supplementals, 'supplemental')
router.register(r'tasks', Tasks, 'task')
router.register(r'technologies', Technologies, 'technology')
router.register(r'wireframes', Wireframes, 'wireframe')
router.register(r'projectcollaborators',ProjectCollaborators, 'projectcollaborator')
router.register(r'projectsupplementals',ProjectSupplementals, 'projectsupplemental')
router.register(r'projecttasks', ProjectTasks, 'projecttask')
router.register(r'projecttechnologies', ProjectTechnologies, 'projecttechnology')
router.register(r'projectwireframes', ProjectWireframes, 'projectwireframe')
router.register(r'projectwireframes', ProjectWireframes, 'projectwireframe')
router.register(r'projects', Projects, 'project')
router.register(r'supplementaltypes', SupplementalTypes, 'supplementaltype')
router.register(r'tasktypes', TaskTypes, 'tasktype')
router.register(r'technologytypes', TechnologyTypes, 'technologytype')
router.register(r'collaboratorinvites', CollaboratorInvites, 'collaboratorinvite')

router.register(r'coders', Coders, 'coder')
router.register(r'users', UserViewSet, 'user')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^admin/', admin.site.urls),
]
