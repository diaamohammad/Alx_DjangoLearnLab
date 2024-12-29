from rest_framework.routers import DefaultRouter
from .views import CommentView,PostView,FeedAPIView,like_post,unlike_post
from django.urls import path


router = DefaultRouter

router.register(r'posts',PostView)
router.register(r'comments',CommentView)

urlpatterns = router.urls + [
    path('feed/',FeedAPIView.as_view(),name = 'feed'),
    path('posts/<int:pk>/like/',like_post,'like'),
    path('posts/<int:pk>/unlike/',unlike_post,'unlike'),
]