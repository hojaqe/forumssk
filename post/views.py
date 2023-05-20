from django.shortcuts import render
from rest_framework import generics, filters
from .models import Comment, Post, Category, Like, Rating
from .serializers import CommentSerializer, PostSerializer, CategorySerializer, LikeSerializer, RatingSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filetrset_fields = ['category', 'author']
    search_fields = ['title','tags__title']
    ordering_fields = ['created_at', 'title']
    # def post_list(request):
    #     query = request.GET.get('q')  # Получаем параметр поиска из URL-строки запроса

    #     if query:
    #         posts = Post.objects.filter(title__icontains=query)  # Фильтруем посты по заданному запросу
    #     else:
    #         posts = Post.objects.all()  # Если запроса нет, отображаем все посты

    #     return render(request, 'post_list.html', {'posts': posts, 'query': query})


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


