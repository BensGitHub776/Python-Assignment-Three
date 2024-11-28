
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from blog.models import Post, Topic, Comment
from django.shortcuts import render
from django.db.models import Count, CharField, Value


#NOTE! a few lines may be incorrectly highlighted as errors if you dont have pylint-django isntalled
def home_view(request):
    '''view for the home page'''
    
    
    topics = Topic.objects.order_by("-name")
    topics= Topic.objects.all()
    posts = Post.objects.all() # returns the top 10 posts
    posts = Post.objects.order_by("title")
    
    
    topic_dict = {}

    #i was having a lot of trouble getting annotations working so i converted the topic data into a dict instead
    for t in topics:
        topic_dict[t.name] = (posts.filter(topic__name=t.name).count())
    print(topic_dict)
    
    
    print(topic_dict)
    print("Test Ping!")

    print("End of Test Ping!")

    print(topics)
    










    comments = Comment.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        "Topics": topic_dict,
        "Posts": posts,
        "Comments": comments
    }

    return HttpResponse(template.render(context, request))

def home(request):
    """
    The Blog homepage
    """
    return render(request, 'about.html')