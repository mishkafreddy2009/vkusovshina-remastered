def test_create_storage(test_client, storage_payload):
    response = test_client.post("/api/storages/", json=storage_payload)
    response_json = response.json()
    assert response.status_code == 201
    response = test_client.get(f"/api/storages/{storage_payload['id']}")
    assert response.status_code == 200
    assert response_json["id"] == storage_payload["id"]
    assert response_json["name"] == storage_payload["name"]
    assert response_json["capacity"] == storage_payload["capacity"]


def test_create_product(test_client, product_payload):
    response = test_client.post(f"/api/products/{product_payload['storage_id']}", json=product_payload)
    response_json = response.json()
    assert response.status_code == 201
    response = test_client.get(f"/api/products/{product_payload['id']}")
    assert response.status_code == 200
    assert response_json["id"] == product_payload["id"]
    assert response_json["name"] == product_payload["name"]
    assert response_json["storage_id"] == product_payload["storage_id"]
    assert response_json["quantity"] == product_payload["quantity"]
