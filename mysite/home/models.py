from django.db import models

class Subscribres(models.Model):
    email = models.CharField(max_length=150, blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title_uz = models.CharField(max_length=200,blank=False,null=False)
    title_en = models.CharField(max_length=200,blank=False,null=False)
    description_uz = models.TextField(blank=False,null=False)
    description_en = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to='images/',blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Followers(models.Model):
    full_name = models.CharField(max_length=200,blank=False,null=False)
    comment_uz = models.TextField(blank=False,null=False)
    comment_en = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

