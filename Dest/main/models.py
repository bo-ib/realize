from django.db import models

from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category_list =models.CharField(max_length=500)

    def __str__(self):
        return self.category_list






class Article(models.Model):
    title = models.CharField(max_length=200)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", null=True,blank=True)
    text = RichTextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post =models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Email =models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self): 
        return  '%s - %s'%(self.Article.title, self.name )

 







