from . import views as base_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', base_views.Feed.as_view(), name='index'),
    path('user/<str:username>', base_views.UserPostView.as_view(), name='user-posts'),
    path('post/<int:pk>/', base_views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', base_views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', base_views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', base_views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', base_views.CommentCreateView.as_view(), name='post-comment'),
    path('comment/<int:pk>/update/', base_views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', base_views.CommentDeleteView.as_view(), name='comment-delete'),
    path('register/', base_views.register, name='register'),
    path('profile/<int:id>/', base_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('search/', base_views.SearchView.as_view(), name='search')
]