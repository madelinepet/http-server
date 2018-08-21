import requests as req


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200
