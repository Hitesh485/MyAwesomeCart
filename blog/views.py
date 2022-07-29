from django.shortcuts import render
from django.http import HttpResponse
from . models import Blogpost   

# Create your views here.
def index(request):
    allPosts = []
    posts = Blogpost.objects.all()
    catprods = Blogpost.objects.values('title', 'head0')
    cats = {item['title'] for item in catprods}
    # print("cats = ", cats)
    for items in range(0, len(cats)):
        # print('items = ', items)
        title = posts[items]
        time = posts[items].pub_date
        chead0 = posts[items].head_content0
        thumbnail = posts[items].thumbnail
        allPosts.append([title, time, chead0, thumbnail])
        
    params = { 'allPosts' : allPosts }
    # print("params = ", params)
    return render(request, 'blog/index.html', params)

def blogpost(request):
    return render(request, 'blog/blogpost.html')