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
    assert '<title>Azure Voting App</title>' in result.get_data(as_text=True)
    assert '<button name="vote" value="Cats" onclick="send()" class="button button1">Cats</button>' in result.get_data(as_text=True)
    assert '<button name="vote" value="Dogs" onclick="send()" class="button button2">Dogs</button>' in result.get_data(as_text=True)

# def test_postError(client):
#     test_client = client[0]
#     result = test_client.post('/')
#     assert result.status_code == 400

# def test_initReset(client):
#     test_client = client[0]
#     result = vote(test_client, "reset")
#     assert result.status_code == 200
#     assert 'Cats - 0 | Dogs - 0' in result.get_data(as_text=True)

# def test_voteCats(client):
#     test_client = client[0]
#     result = vote(test_client, "Cats")
#     assert result.status_code == 200
#     assert 'Cats - 1 | Dogs - 0' in result.get_data(as_text=True)

# def test_voteDogs(client):
#     test_client = client[0]
#     result = vote(test_client, "Dogs")
#     result = vote(test_client, "Dogs")
#     assert result.status_code == 200
#     assert 'Cats - 1 | Dogs - 2' in result.get_data(as_text=True)

# def test_reset(client):
#     test_client = client[0]
#     result = vote(test_client, "reset")
#     assert result.status_code == 200
#     assert 'Cats - 0 | Dogs - 0' in result.get_data(as_text=True)

# def test_redisConnectoin(client):
#     with patch.dict("os.environ", {"REDIS": "errorhost"}):
#         test_client = client[0]
#         result = vote(test_client, "reset")
#         print(result)
#     assert 'Cats - 0 | Dogs - a' in result.get_data(as_text=True)
