from django.urls import path, include
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth.decorators import login_required



urlpatterns = [
    
    #API urls
    path("", ListArticle.as_view()),
    path("create", CreateArticle.as_view()),
    path('register', RegisterUserAPIView.as_view()),
    path("get-details", UserDetailAPI.as_view()),
    path("<pk>", RetrieveUpdateDeleteArticle.as_view()),
    
    
]

#Try to access Urls of API from API folder so that it can be mmanaged effectively
    