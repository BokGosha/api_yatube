from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
