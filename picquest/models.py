from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    image = CloudinaryField('image')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts", null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='like', blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def number_of_likes(self):
        return self.likes.count()
    