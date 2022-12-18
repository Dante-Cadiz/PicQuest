from django.shortcuts import render, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks
from .models import Post
from .forms import PostForm

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


def AddPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = PostForm()
    return render(request, 'create_post.html', {'form': form})


#class EditPost(View):
    #def post(self, request, slug, *args, **kwargs):

#class DeletePost(View):
    #def post(self, request, slug, *args, **kwargs):