from rest_framework.routers import DefaultRouter
from .views import CommentView,PostView,FeedAPIView
from django.urls import path


router = DefaultRouter

router.register(r'posts',PostView)
router.register(r'comments',CommentView)

urlpatterns = router.urls + [
    path('feed/',FeedAPIView.as_view(),name = 'feed')
]