from rest_framework.routers import DefaultRouter
from .views import CommentView,PostView

router = DefaultRouter

router.register(r'posts',PostView)
router.register(r'comments',CommentView)

urlpatterns = router.urls