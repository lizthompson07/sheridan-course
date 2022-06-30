"""views"""

# blog/views.py

from django.shortcuts import render
from . import models


def home(request):
    """
    The Blog homepage
    """
    # Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]

    # Get authors
    authors = models.Post.objects.published().get_authors().order_by('first_name')

    # Get top 10 posts
    top_10 = models.Post.objects.published()[0:10]
    topics = top_10.get_number_posts_by_topic()
    # Add as context variable "latest_posts"
    context = {
        'topics': topics,
        'authors': authors,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)
