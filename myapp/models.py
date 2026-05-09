from django.db import models

"""
class Collection(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField
"""

class Mytodo(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=250)


class Meta: 
    ordering = ['-created_at']


    def __str__(self):
        return self.title


