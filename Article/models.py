from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    Author = models.CharField(max_length=20)
    Publish_date = models.DateField()

    def __str__(self):
        return self.Author

    def get_absolute_url(self):   
        return reverse("listing")  #redirect to url name listing after successfully posting resource