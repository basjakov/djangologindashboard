from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    longText = models.TextField(max_length=800)
    date = models.DateTimeField()