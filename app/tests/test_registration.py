import uuid


def test_create_user(test_app):
    response = test_app.post("/create_user")
    assert response.status_code == 201
    response_json = response.json()
    assert response_json.get('user_id') and type(response_json.get('user_id')) == int and response_json.get(
        'user_id') > 0
    assert response_json.get('name') and type(response_json.get('name')) == str
    assert response_json.get('uuid') and uuid.UUID(str(response_json['uuid']))
