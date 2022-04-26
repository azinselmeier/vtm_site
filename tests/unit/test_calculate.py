def test_add_inputs(app,client):
    """
    GIVEN a user enters inputs
    WHEN the function calculates an estimate from the inputs
    THEN the estimate is calculated accurately
    """
    with app.test_client() as test_client:
        calculate = {"radius":"180", "height":"360"} 
        res = test_client.post('/add_inputs', data=calculate)
        assert res.status_code == 404
        assert b"141300.00000000003" in res.data
