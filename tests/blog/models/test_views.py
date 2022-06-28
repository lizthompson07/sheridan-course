"""Test Views"""
import pytest
from model_mommy import mommy

# def test_index():
#     """Basic Test with fail"""
#     assert False  # This is must fail
#
#
# def test_index_ok(client):
#     """Basic Test with fail"""
#     response = client.get('/banana')  # Doesn't exist
#     assert response.status_code == 200
from blog.models import Post


@pytest.mark.django_db
def test_home_ok(client):
    """Basic test"""
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200


def test_authors_included_in_context_data(client, django_user_model):
    """
    Checks that a list of unique published authors is included in the
    context and is ordered by first name.
    """
    # Make a published author called Cosmo
    cosmo = mommy.make(
        django_user_model,
        username='ckramer',
        first_name='Cosmo',
        last_name='Kramer'
    )
    mommy.make(
        'blog.Post',
        status=Post.PUBLISHED,
        author=cosmo,
        _quantity=2
    )
    # Make a published author called Elaine
    elaine = mommy.make(
        django_user_model,
        username='ebenez',
        first_name='Elaine',
        last_name='Benez'
    )
    mommy.make(
        'blog.Post',
        status=Post.PUBLISHED,
        author=elaine,
    )

    # Make an unpublished author
    unpublished_author = mommy.make(
        django_user_model,
        username='gcostanza'
    )
    mommy.make('blog.Post', author=unpublished_author, status=Post.DRAFT)

    # Expect Cosmo and Elaine to be returned, in this order
    expected = [cosmo, elaine]

    # Make a request to the home view
    response = client.get('/')

    # The context is available in the test response.
    result = response.context.get('authors')

    # Cast result (QuerySet) to a list to compare
    assert list(result) == expected
