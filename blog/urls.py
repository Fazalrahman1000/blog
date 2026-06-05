from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsList.as_view(), name='posts'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('create-post/', views.CreatePost.as_view(), name='create_post'),
    path('edit-post/<slug:slug>/', views.EditPost.as_view(), name='edit_post'),
    path('delete-post/<slug:slug>/', views.DeletePost.as_view(), name='delete_post'),
    path('post/<slug:slug>/comment/', views.AddComment.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete_comment'),
    path('category/<slug:slug>/', views.CategoryPosts.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', views.TagPosts.as_view(), name='tag_posts'),
]