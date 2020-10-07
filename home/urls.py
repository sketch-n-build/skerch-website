from django.urls import path
from home import views as home_views
from .views import PostsDetailView, PostDeleteView,PostListView,UserPostListView,home_view

urlpatterns = [
    path('', home_view,name='home'),
    path('user/<str:username>/', UserPostListView.as_view(),name='user-post'),
    path('about/', home_views.about,name='about'),
    path('blog/', PostListView.as_view(),name='blog'),
    path('post/', home_views.create_post,name='post'),
    path('post/<int:pk>/detail/',PostsDetailView.as_view(),name='post-details'),
    path('post/<int:pk>/update/',home_views.post_update,name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]