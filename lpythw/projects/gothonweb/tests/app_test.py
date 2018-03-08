from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_not_equals(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equals(rv.status_code, 200)
    assert_in(b"Gothons Of Planet Percal #25", rv.data)

    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/greet', follow_redirects=True, data=data)
    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)


