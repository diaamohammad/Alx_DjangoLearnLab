from django.urls import path
from .views import RegisterApiView,LoginApiView,ProfileApiView,FollowUser,UnFollowUser

urlpatterns = [
    path('register/',RegisterApiView.as_view(),name = 'register'),
    path('login/',LoginApiView.as_view(),name = 'login'),
    path('profile/',ProfileApiView.as_view(),name = 'profile'),
    path('follow/<int:user_id>/',FollowUser.as_view(),name = 'follow'),
    path('unfollow/<int:user_id>/',UnFollowUser.as_view(),name = 'unfollow'),

]