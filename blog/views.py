"""views"""

# blog/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from . import models


# Replaced with context processor
# class ContextMixin:
#     """
#     Provides common context variables for blog views
#     """
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['authors'] = models.Post.objects.published() \
#             .get_authors() \
#             .order_by('first_name')
#
#         # Define "topics" context variable
#         top_10 = models.Post.objects.published()[0:10]
#
#         context['topics'] = top_10.get_number_posts_by_topic()
#
#         return context


def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')


class HomeView(TemplateView):
    """
    The blog homepage
    """
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)

        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]

        # Update the context with our context variables
        context.update({
            'latest_posts': latest_posts
        })

        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'

# POSTS #


class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')  # Customized queryset


class PostDetailView(DetailView):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset().published()

        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )


# TOPICS #


class TopicListView(ListView):
    model = models.Topic
    context_object_name = 'all_topics'  # make sure this isn't the same as in context_processors

    # get just the list of topics from posts that have been published
    queryset = models.Topic.objects.filter(blog_posts__status='published').distinct().order_by('name')


class TopicDetailView(DetailView):
    model = models.Topic

    # def get_queryset(self):
    #     queryset = super().get_queryset().published()
    #
    #     # Filter on the topic
    #     return queryset.filter(
    #         topics__slug=self.kwargs['slug'],
    #     )

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)

        posts_by_topic = models.Post.objects.published().filter(topics__slug=self.kwargs['slug'])

        # Update the context with our context variables
        context.update({
            'posts_by_topic': posts_by_topic
        })

        return context
