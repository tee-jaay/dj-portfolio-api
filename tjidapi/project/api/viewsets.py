from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ProjectSerializers, CategorySerializers
from ..models import Project, Category


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(status='publish').order_by('-created')
    serializer_class = ProjectSerializers

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        details = request.data['details']
        image = request.data['image']
        status = request.data['status']
        url = request.data['url']
        slug = request.data['slug']
        category = request.data['category']
        Project.objects.create(title=title, details=details, image=image, status=status, url=url, slug=slug,
                               category=category)
        return HttpResponse({'message': 'Project created'}, status=200)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status='publish')
    serializer_class = CategorySerializers
