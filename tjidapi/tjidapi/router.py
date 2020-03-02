from rest_framework import routers

from project.api.viewsets import CategoryViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)
router.register('category', CategoryViewSet)
