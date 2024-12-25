from rest_framework.routers import DefaultRouter
from .views import CommentView,PostView

router = DefaultRouter

router.register(r'api/posts',PostView)
router.register(r'api/comments',CommentView)

urlpatterns = router.urls