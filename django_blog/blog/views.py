from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, CustomUserCreationForm  # تأكد من أن PostForm و CustomUserCreationForm موجودين في الفورمز
from .models import Post
from django.contrib.auth.decorators import login_required

# View for listing all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/Post_List.html'
    context_object_name = 'posts'


# View for creating a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/Post_Create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # تأكد من أنه يتم تحديد المؤلف (author)
        return super().form_valid(form)


# View for displaying a post's details
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/Post_detail.html'
    context_object_name = 'post'


# View for updating an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/Post_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user  # تأكد من أنه يمكن فقط للمؤلف تعديل المشاركة


# View for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/Post_delete.html'
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user  # تأكد من أنه يمكن فقط للمؤلف حذف المشاركة


# Function for creating a post (using a form instead of a class-based view)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'blog/Post_Create.html', {'form': form})


# Custom login view
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'


# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


# Register view for user sign-up
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# User profile view to update email
@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})
