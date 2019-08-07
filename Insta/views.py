from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # may be delete this .just test
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

class PostUpdateView(UpdateView):
    model = Post
    template_name= 'post_edit.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name= 'post_delete.html'
    success_url = reverse_lazy('posts')  #用lazy版是防止circular import的问题
    # success_url 是说当delete成功后应该跳转到哪里

class SignUp(CreateView):
    #model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


