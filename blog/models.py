from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner_image = models.ImageField(upload_to='blog') 

    def __str__(self):
        return self.title