from django.shortcuts import render
from django.views import generic, View
from .models import Post

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class PostList(generic.ListView):
    template_name = "posts.html"
    model = Post #temporary until filter created for today's posts only
    paginate_by = 6

#class YourPosts(View):
    #def get(self, request, *args, **kwargs):
        #your_posts = Post.objects.filter(
         #       author=self.request.user.id).order_by('created_on')
        #return render(
            #request, "your_posts.html",
            #{
               # "your_posts": your_posts,
           # },)
#class AddPost(View):
    #def post(self, request, slug, *args, **kwargs):

#class EditPost(View):
    #def post(self, request, slug, *args, **kwargs):

#class DeletePost(View):
    #def post(self, request, slug, *args, **kwargs):