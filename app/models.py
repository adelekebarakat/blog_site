from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='compulsory')
    body = models.TextField(help_text='compulsory')
    image = models.ImageField(upload_to ='media/', help_text='compulsory')
    rating = models.IntegerField()

    def __str__(self):
        return self.title



