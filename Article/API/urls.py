from django.urls import path
from .views import *


urlpatterns = [
    path("api/list", ListCreateArticle.as_view()),
    path("api/single/<id>", RetrieveUpdateDeleteArticle.as_view()),
]