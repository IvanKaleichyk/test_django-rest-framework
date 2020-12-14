from django.test import TestCase

from django.contrib.auth.models import User

from .models import *


class BlogTests(TestCase):
    # user
    userName = 'Ivan'
    password = 'abc123'

    # title
    title = 'Blog title'
    body = 'Body content...'

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username='Ivan',
            password='abc123'
        )
        test_user1.save()

        test_post = Post.objects.create(
            author=test_user1,
            title='Blog title',
            body='Body content...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'Ivan')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')
