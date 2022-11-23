from django.urls import path
from .views import *


urlpatterns = [
    path("", ShowArticle.as_view(), name="listing"),
    path("detail/<pk>", SingleArticle.as_view()),
    path("create/", NewBlogEntry.as_view()),
    path("detail/update/<pk>", Modifyarticle.as_view()),  #simplify url pattern
    path("detail/delete/<pk>", RemoveArticle.as_view())
]