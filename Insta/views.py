from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post, InstaUser, Like, Comment, UserConnection
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from annoying.decorators import ajax_request
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


class UserDetailView(DetailView):
        model = InstaUser
        template_name = 'user_detail.html'
        #login_url = 'login'

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }

@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }

@ajax_request
def toggleFollow(request):
    current_user = InstaUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = InstaUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(creator=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }