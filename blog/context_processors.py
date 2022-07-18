# blog/context_processors.py


from . import models


def base_context(request):
    # authors of published
    authors = models.Post.objects.published() \
        .get_authors() \
        .order_by('first_name')

    # top 10 topics
    top_10 = models.Post.objects.published()[0:10]
    topics = top_10.get_number_posts_by_topic().order_by('name')

    return {'authors': authors, 'topics': topics}

