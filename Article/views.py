from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.http import HttpResponseRedirect

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