from rest_framework import serializers
from ..models import Project, Category


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'details', 'image', 'status', 'url', 'slug', 'category')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'count', 'slug', 'status')
