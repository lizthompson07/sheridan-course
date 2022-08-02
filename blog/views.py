"""views"""

# blog/views.py
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.views.generic.base import TemplateView
from . import models, forms


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


# Example of function-based form view

# def form_example(request):
#     # Handle the POST
#     if request.method == 'POST':
#         # Pass the POST data into a new form instance for validation
#         form = forms.ExampleSignupForm(request.POST)
#
#         # If the form is valid, return a different template.
#         if form.is_valid():
#             # form.cleaned_data is a dict with valid form data
#             cleaned_data = form.cleaned_data
#
#             return render(
#                 request,
#                 'blog/form_example_success.html',
#                 context={'data': cleaned_data}
#             )
#     # If not a POST, return a blank form
#     else:
#         form = forms.ExampleSignupForm()
#
#     # Return if either an invalid POST or a GET
#     return render(request, 'blog/form_example.html', context={'form': form})


class FormViewExample(FormView):
    template_name = 'blog/form_example.html'
    form_class = forms.ExampleSignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Create a "success" message
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for signing up!'
        )
        # Continue with default behaviour
        return super().form_valid(form)


class ContactFormView(CreateView):
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)


class ContestFormView(CreateView):
    model = models.Contest
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'photo',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your contest submission has been sent.'
        )
        return super().form_valid(form)


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
