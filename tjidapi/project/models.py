from django.db import models

# Publish status
STATUS = (
    ('draft', 'Draft'),
    ('publish', 'Publish')
)


# Project's Category
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, default='publish')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# Project image upload path
# def upload_path(instance, filename):
#     return '/'.join(['projects', str(instance.title), filename])


# Project
class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='project/%Y/%m/%d/')
    # image = models.ImageField(null=True, blank=True, upload_to=upload_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
