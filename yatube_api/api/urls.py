from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('posts/<int:post_id>', PostViewSet, basename='post')
router.register('posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls))
]
