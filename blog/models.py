from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=70)

    slug = models.SlugField(unique=True)

    def __str__(self):

        return self.name
    
    class Meta:

        ordering = ['name']



class Tag(models.Model):

    tagName = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.tagName
    
    class Meta:
        ordering = ['tagName']
    


    
class Post(models.Model):

    title = models.CharField(max_length=500)

    slug = models.SlugField(unique=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    tag = models.ManyToManyField(Tag, blank=True)

    featured_img = models.ImageField(upload_to='posts', null=True, blank=True)

    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    



class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete = models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.post}"
    
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # one like per user per post

    def __str__(self):
        return f"{self.user} liked {self.post}"