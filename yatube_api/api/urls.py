from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('posts/<int:post_id>', PostViewSet, basename='post')
router.register('posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register('following', FollowViewSet, basename='following')
router.register('following/<int:author_id>', FollowViewSet, basename='followings')
router.register('groups', GroupViewSet, basename='groups')
router.register('groups/<str:slug>', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls))
]
