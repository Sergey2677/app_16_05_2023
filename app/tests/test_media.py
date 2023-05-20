def test_add_media(test_app):
    response = test_app.post("/add_media")
    assert response.status_code == 200
    # response_json = response.json()
