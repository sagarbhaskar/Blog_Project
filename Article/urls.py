from django.urls import path, include
from .API import views,urls
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("", ShowArticle.as_view(), name="listing"),
    path("detail/<pk>", SingleArticle.as_view()),
    path("create/", login_required(NewBlogEntry.as_view())),
    path("detail/update/<pk>", login_required(Modifyarticle.as_view())),  #simplify url pattern
    path("detail/delete/<pk>", login_required(RemoveArticle.as_view())),

    #login urls
    path("signup/", Signup_View),
    path("logout", Logout_View),
    
    #API urls
    path("api/", views.ListArticle.as_view()),
    path("api/create", views.CreateArticle.as_view()),
    path("api/<pk>", views.RetrieveUpdateDeleteArticle.as_view()),

    #JWT Authentication urls
    path("auth-jwt/", obtain_jwt_token),
    path('auth-jwt-refresh', refresh_jwt_token),
    path('auth-jwt-verify', verify_jwt_token)
]

#Try to access Urls of API from API folder so that it can be mmanaged effectively
    