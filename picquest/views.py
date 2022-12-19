from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    model = Post
    #liked = False
    #if Post.likes.filter(id=self.request.user.id).exists():
        #liked = True 
    paginate_by = 6

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['likes'] = Post.likes()
        #return context

class YourPosts(View):
    def get(self, request, *args, **kwargs):
        your_posts = Post.objects.filter(
               author=self.request.user.id).order_by('created_on')
        return render(
            request, "your_posts.html",
            {
                "your_posts": your_posts,
            },)


def AddPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.author = request.user.id
            form.save()
            return redirect('posts')
    
    form = PostForm()
    return render(request, 'create_post.html', {'form': form})


#class EditPost(View):
    #def post(self, request, slug, *args, **kwargs):

#class DeletePost(View):
    #def post(self, request, slug, *args, **kwargs):

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('posts'))