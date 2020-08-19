from django.urls import path
from . import views


urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<pk>/', views.PostDetailView, name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<pk>/likepost/',views.likePost,name='likepost'),
]
