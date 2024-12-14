from . views import profile_view,register_view,CustomLoginView,CustomLogoutView,PostListView,PostCreateView,PostDeleteView,PostDetailView,PostUpdateView
from django.urls import path

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view(), name = 'post-list'),
    path('post/new/', PostCreateView.as_view(), name= 'post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
        
    
]