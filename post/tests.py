from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category, Comment, Like, Rating
from rest_framework.test import APITestCase, APIRequestFactory

class PostTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title='cat1')
        user = User.objects.create_user(email='user@gmail.com', password='12345', is_active=True, name='test')
        self.token ='12345'
        posts = [
            Post(author=user, body='new post2', title = 'post2', category=self.category)
        ]
        Post.objects.bulk_create(posts)
        

class CommentTestCase(TestCase):
    def test_create_comment(self):
        post = Post.objects.create(title='Test Post', content='This is a test post')
        response = self.client.post('/create_comment/', {'post_id': post.id, 'comment': 'Test comment'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)


class LikeTestCase(TestCase):
    def test_like_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post')
        response = self.client.post('/like_post/', {'post_id': post.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Like.objects.count(), 1)


class RatingTestCase(TestCase):
    def test_post_rating(self):
        post = Post.objects.create(title='Test Post', content='This is a test post')
        post.rate(5) 
        self.assertEqual(post.rating, 5)
        self.assertEqual(Rating.objects.count(), 1)