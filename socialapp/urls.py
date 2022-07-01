from . import views as socialapp_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', socialapp_views.Feed.as_view(), name='index'),
    path('user/<str:username>', socialapp_views.UserPostView.as_view(), name='user-posts'),
    path('post/<int:pk>/', socialapp_views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', socialapp_views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', socialapp_views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', socialapp_views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', socialapp_views.CommentCreateView.as_view(), name='post-comment'),
    path('comment/<int:pk>/update/', socialapp_views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', socialapp_views.CommentDeleteView.as_view(), name='comment-delete'),
    path('register/', socialapp_views.register, name='register'),
    path('profile/<int:id>/', socialapp_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='socialapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='socialapp/logout.html'), name='logout'),
    path('search/', socialapp_views.SearchView.as_view(), name='search')
]