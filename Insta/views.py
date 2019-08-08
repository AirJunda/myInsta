from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post, InstaUser
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User # m多余的。是我认为需要额外添加user model时按操作加的

# below is for 个性化用户设置
from Insta.models import InstaUser
from Insta.forms import CustomUserCreationForm
# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'examplepage.html'

class PostsView(ListView):
    model= Post
    template_name='index.html'   #page to list and to present posts

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreatView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'  #提供所有field
    login_url = 'login'  # 加入这个。那么post时候会导向login page.这样以保证只有login才能post
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
    #model = InstaUser
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


