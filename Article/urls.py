from django.urls import path, include
from .API import views,urls
from .views import *



urlpatterns = [
    path("", ShowArticle.as_view(), name="listing"),
    path("detail/<pk>", SingleArticle.as_view()),
    path("create/", NewBlogEntry.as_view()),
    path("detail/update/<pk>", Modifyarticle.as_view()),  #simplify url pattern
    path("detail/delete/<pk>", RemoveArticle.as_view()),
    
    #API urls
    path("api/", views.ListCreateArticle.as_view()),
    path("api/<pk>", views.RetrieveUpdateDeleteArticle.as_view()),
]

#Try to access Urls of API from API folder so that it can be mmanaged effectively
    