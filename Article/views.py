from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.conf import settings


from django.contrib.auth import get_user_model

User = get_user_model()

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

def Signup_View(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request, 'registration/signup.html', {'form':form})

def Logout_View(request):
    return render(request, "registration/logout.html")



def MyBlogs_View(request):

    """ query not worked, tried to find the blogs of the singl user (blogs created by user who is logged in)
    #qs = Article.objects.filter(Article.author_id == request.user)  
    """
    qs= request.user.article_set.all()   #requet.user--> fetching information about particular user
    #print(qs)
    return render(request, "Article/myblogs.html", {'qs': qs})