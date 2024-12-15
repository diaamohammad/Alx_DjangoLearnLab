from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, CustomUserCreationForm ,CommentForm 
from .models import Post,Comment
from django.contrib.auth.decorators import login_required

# View for listing all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


# View for creating a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # تأكد من أنه يتم تحديد المؤلف (author)
        return super().form_valid(form)


# View for displaying a post's details
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# View for updating an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user  # تأكد من أنه يمكن فقط للمؤلف تعديل المشاركة


# View for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
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
    return render(request, 'blog/post_create.html', {'form': form})


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

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':  # إضافة تعليق جديد
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', post_id=post.id)
        else:
            return redirect('login')  
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})



@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('post_detail', post_id=comment.post.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    return redirect('post_detail', post_id=comment.post.id)
