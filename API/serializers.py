from Article.models import Article
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields= "__all__"


class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"


class RegisterSerializer(ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  
  class Meta:
    model = User
    fields = "__all__"
         
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user