from django.urls import path, include
from .views import CommentListCreateView, PostListCreateView, CategoryListCreateView, CommentRetrieveUpdateDestroyView, PostRetrieveUpdateDestroyView, CategoryRetrieveUpdateDestroyView, LikeListCreateView, RatingListCreateView


urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('posts/likes/', LikeListCreateView.as_view()),
    path('posts/rating/', RatingListCreateView.as_view()),    
]