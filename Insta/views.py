from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'examplepage.html'

class PostsView(ListView):
    model= Post
    template_name='index.html'   #page to list and to present posts

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreatView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'  #提供所有field

