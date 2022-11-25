from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','Author','author_id','Title', 'description',  'Publish_date']

admin.site.register(Article, ArticleAdmin)