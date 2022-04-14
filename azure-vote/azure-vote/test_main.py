"""Test Code"""
import pytest

from main import app


@pytest.fixture()
def client(request):
    app.config['TESTING'] = True
    test_client = app.test_client()
    yield test_client
    test_client.delete()


def vote(client, vote):
    return client.post('/', data=dict(vote=vote), follow_redirects=True)


def test_get(client):
    test_client = client
    result = test_client.get('/')
    assert result.status_code == 200
    assert 'Azure Voting App' in result.get_data(as_text=True)
    assert 'Cats' in result.get_data(as_text=True)
    assert 'Dogs' in result.get_data(as_text=True)


def test_postError(client):
    with pytest.raises(Exception) as e:
        test_client = client
        _ = test_client.post('/')
    assert str(e.value) == "400 Bad Request: The browser (or proxy) sent a request that this server could not understand.\nKeyError: 'vote'"        

# def test_Fail(client):
#     assert False
