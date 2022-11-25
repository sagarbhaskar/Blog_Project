from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from Article.models import Article
from .serializers import ArticleSerializer, RegisterSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User

class ListArticle(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny,]
    #authentication_classes = [TokenAuthentication]

class CreateArticle(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]

class RetrieveUpdateDeleteArticle(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]

# Class based view to Get User Details using JWT Authentication
class UserDetailAPI(APIView):
  authentication_classes = [JSONWebTokenAuthentication,]
  permission_classes = [AllowAny,]

  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer