from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Article.models import Article
from .serializers import ArticleSerializer

class ListCreateArticle(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #authentication_classes = [TokenAuthentication]

class RetrieveUpdateDeleteArticle(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer