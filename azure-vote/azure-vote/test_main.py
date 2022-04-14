"""Test Code"""
import pytest, os

from main import app

from unittest.mock import patch

@pytest.fixture(params=[("req1","res1")])
def client(request):
    app.config['TESTING'] = True
    test_client = app.test_client()
    yield test_client, request.param
    test_client.delete()

def vote(client, vote):
    return client.post('/',data=dict(vote=vote), follow_redirects=True)


def test_get(client):
    test_client = client[0]
    result = test_client.get('/')
    assert result.status_code == 200
    assert 'Azure Voting App' in result.get_data(as_text=True)
    assert 'Cats' in result.get_data(as_text=True)
    assert 'Dogs' in result.get_data(as_text=True)

# def test_Fail(client):
#     assert False

