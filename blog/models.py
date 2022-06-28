"""Models"""
from django.conf import settings # Imports Django's loaded settings
from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth import get_user_model


class Topic(models.Model):
    """
    Model for topics.
    """
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        """For ordering"""
        ordering = ['name']


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

    def draft(self):
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        User = get_user_model()
        # Get the users who are authors of this queryset
        return User.objects.filter(blog_posts__in=self).distinct()


class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    objects = PostQuerySet.as_manager()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',  # "This" on the user model
        null=False,
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        null=False,
        help_text='The date & time this article was published',
        unique_for_date='published',  # Slug is unique for publication date
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )
    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    class Meta:
        """Define ordering"""
        # Sort by the `created` field. The `-` prefix
        # specifies to order in descending/reverse order.
        # Otherwise, it will be in ascending order.
        ordering = ['-created']

    def __str__(self):
        return self.title

    def publish(self):
        """Publishes this post"""
        self.status = self.PUBLISHED
        self.published = timezone.now()  # The current datetime with timezone


class Comment(models.Model):
    """
    Represents a comment post
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,  # Prevent comments from being deleted
        related_name='comments',  # "This" on the post model
        null=False,
    )
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='comment_posts',  # "This" on the user model
        null=False,
    )
    email = models.EmailField()
    text = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    def __str__(self):
        return self.text

    class Meta:
        """For ordering"""
        ordering = ['-created']
