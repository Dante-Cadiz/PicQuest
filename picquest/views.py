from django.shortcuts import render
from django.views import generic, View

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PostList(generic.ListView):
    template_name = ""
    paginate_by = 6

#class AddPost(View):
    #def post(self, request, slug, *args, **kwargs):

#class EditPost(View):
    #def post(self, request, slug, *args, **kwargs):

#class DeletePost(View):
    #def post(self, request, slug, *args, **kwargs):