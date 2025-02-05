from django.db import models
from authentification.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    #content = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    hot_item = models.CharField(max_length=100, default="crypto")
    def __str__(self):
        return self.title

    
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name

class Blogs_Categories(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    #def __str__(self):
      #  return self.category_id + ' ' + self.blog_id
    
