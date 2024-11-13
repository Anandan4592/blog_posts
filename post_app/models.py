from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)
    attachment = models.ImageField(upload_to='Image/',null=True)

