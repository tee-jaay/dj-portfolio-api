from django.contrib import admin

from .models import Project, Category


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'details', 'image', 'status', 'url', 'slug', 'category']


admin.site.register(Project, ProjectAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'count', 'slug', 'status']


admin.site.register(Category, CategoryAdmin)
