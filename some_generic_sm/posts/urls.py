from django.urls import path
from some_generic_sm.posts.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<uuid:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
