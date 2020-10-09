from django.urls import path
from home import views as home_views
from .views import PostListView,PostsDetailView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', home_views.home_view,name='home'),
    path('user/<str:username>/', UserPostListView.as_view(),name='user-post'),
    path('user/', home_views.user,name='user'),
    path('leaderbord/', home_views.leaderboard,name='leaderboard'),
    path('about/', home_views.about,name='about'),
    path('contact/', home_views.contact_us,name='contact'),
    path('speakers/', home_views.speakers,name='speakers'),
    path('schedule/', home_views.schedule,name='schedule'),
    path('blog/', PostListView.as_view(),name='blog'),
    path('post/', home_views.create_post,name='post'),
    path('post/<int:pk>/detail/',PostsDetailView.as_view(),name='post-details'),
    path('post/<int:pk>/update/',home_views.post_update,name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]