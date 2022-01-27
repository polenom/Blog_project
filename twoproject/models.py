from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    created= models.DateTimeField(default=timezone.now)
    link = models.CharField( max_length=300,blank=True, null= True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-created']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='adm' ,on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    text = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Person(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Newper(models.Model):
    l = models.CharField(max_length=120)

    def __str__(self):
        return self.l
