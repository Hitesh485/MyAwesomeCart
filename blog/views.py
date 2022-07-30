from django.shortcuts import render
from django.http import HttpResponse
from . models import Blogpost   

# Create your views here.
def index(request):
    allPosts = []
    posts = Blogpost.objects.all()
    # print(posts)
    params = { 'allPosts' : posts }
    return render(request, 'blog/index.html', params)

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print("post = ", post)
    return render(request, 'blog/blogpost.html', {'post': post})