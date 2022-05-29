"""Test Views"""


# def test_index():
#     """Basic Test with fail"""
#     assert False  # This is must fail
#
#
# def test_index_ok(client):
#     """Basic Test with fail"""
#     response = client.get('/banana')  # Doesn't exist
#     assert response.status_code == 200


def test_index_ok(client):
    """Basic test"""
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200
