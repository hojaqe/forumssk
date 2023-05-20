from django.db import models
from config.models import User

class Category(models.Model):
    name = models.CharField(max_length=101)
    slug = models.SlugField(max_length=101)


    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=101)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.title

    
class Comment(models.Model):
    title = models.CharField(max_length=101)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content[:50]
    

class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.post} - {self.rating}'


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self) -> str:
        return f'Liked {self.post} by {self.author.name}'
