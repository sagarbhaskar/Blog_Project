from django.db import models
from django.urls import reverse
from django.conf import settings



# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    Author = models.CharField(max_length=20)
    Publish_date = models.DateField()
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, to_field="id")


    def __str__(self):
        return self.Author

    def get_absolute_url(self):   
        return reverse("listing")  #redirect to url name listing after successfully posting resource