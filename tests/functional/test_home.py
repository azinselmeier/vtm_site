def test_index_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client/get('/')
        assert res.status_code == 200

def test_about_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client/get('/about')
        assert res.status_code == 302

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client/get('/estimate')
        assert res.status_code == 302

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        estimate = {"height":"360", "radius":"180"}
        assert res.status_code == 302