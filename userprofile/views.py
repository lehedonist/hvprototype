from django.http import HttpResponse,HttpResponseNotFound
from .models import User, Post, Product
from django.views import generic
from django.shortcuts import render

class ProfileView(generic.DetailView):
	model = User
	template_name ='userprofile/index.html'

class PostView(generic.DetailView):
	model = Post
	template_name ='userprofile/post.html'

def HomeView(request):
    return render(request, 'userprofile/home.html', {})

class ProductView(generic.DetailView):
	model = Product
