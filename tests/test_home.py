import pytest

def test_home(client):
    response = client.get('/')
    assert b'Welcome' in response.data
