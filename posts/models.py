from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Post(models.Model):
  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-image_qpztio', blank=True
    )

    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
