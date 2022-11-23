from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.

class ShowArticle(ListView):
    model = Article
    context_object_name = "Article_list"

class SingleArticle(DetailView):
    model = Article
    #context_object_name = "obj"

class NewBlogEntry(CreateView):
    model = Article
    fields= "__all__"    #needs fields attribute

class Modifyarticle(UpdateView):
    model = Article
    fields= "__all__"    #needs fields attribute

class RemoveArticle(DeleteView):
    model = Article
    success_url = reverse_lazy("listing")