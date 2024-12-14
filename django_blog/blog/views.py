
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from . forms import CustomUserCreationForm,PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class CustomLoginView(LoginView):

    template_name='login.html'

class CustomLogoutView(LogoutView):

    template_name='logout.html'

def register_view(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login = (request,user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm
    return render(request,'register.html',{'form':form})

@login_required
def profile_view(request):

    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request,'profile.html',{'user':request.user})


class PostListView(ListView):
    model= Post
    template_name = 'Post_List.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'Post_Create.html'
    fields = ['title','content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'Post_detail.html'
    context_object_name = 'post'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'Post_update.html'
    fields = ['title','content']
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'Post_delete.html'
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

def create_post(request):

    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')
    else:
        form = PostForm()
        return render(request,'Post_Create.html',{'form':form})
    
