import requests as req


def test_server_get_home_route_status_200():
    """
    GET /: 200 OK <HTML Response>
    """
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000')
    assert '<html><body><h1>Hello world</h1></body></html>' == str(response.text)
    assert 'Hello world' in str(response.text)


def test_server_get_cow_route_status_200():
    """
    GET /cow?msg=text: 200 OK <Text Response>
    """
    response = req.get('http://127.0.0.1:5000/cow?msg=txt')
    assert response.status_code == 200


def test_server_get_cow_route_status_400():
    """
    GET /cow: 400 Bad Request
    """
    response = req.get('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_server_get_cow_route_status_400_multiple_keys():
    """
    GET /cow?who=dat&wat=do: 400 Bad Request
    """
    response = req.get('http://127.0.0.1:5000/cow?who=dat&wat=do')
    assert response.status_code == 400


def test_server_get_cow_route_status_405():
    """
    !GET /cow?msg=text: 405 Invalid Method
    """
    response = req.get('http://127.0.0.1:5000/cow?msg=text')
    assert response.status_code == 405


def test_server_post_cow_route_status_201():
    """
    POST /cow msg=text: 201 Created <JSON Response>
    """
    response = req.post('http://127.0.0.1:5000/cow msg=text')
    assert response.status_code == 201


def test_server_post_cow_route_status_400():
    """
    POST /cow: 400 Bad Request
    """
    response = req.post('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_server_post_cow_route_status_400_multiple_keys():
    """
    POST /cow who=this how=why: 400 Bad Request
    """
    response = req.post('http://127.0.0.1:5000/cow who=this how=why')
    assert response.status_code == 400


def test_server_post_cow_route_status_404():
    """
    ANY /does_not_exist: 404 Not Found
    """
    response = req.post('http://127.0.0.1:5000/does_not_exist')
    assert response.status_code == 404














