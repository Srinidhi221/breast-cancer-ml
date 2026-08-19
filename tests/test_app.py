import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"API is running" in response.data

def test_predict_valid_input(client):
    # 30 dummy feature values matching the Breast Cancer Wisconsin dataset shape
    sample_features = [14.0, 20.0, 90.0, 600.0, 0.1, 0.15, 0.1, 0.05, 0.2, 0.06,
                        0.4, 1.0, 3.0, 40.0, 0.005, 0.02, 0.02, 0.01, 0.02, 0.003,
                        16.0, 25.0, 105.0, 800.0, 0.14, 0.3, 0.3, 0.12, 0.3, 0.08]
    response = client.post("/predict", json={"features": sample_features})
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data
    assert "result" in data
    assert data["result"] in ["Malignant", "Benign"]

def test_predict_missing_features_key(client):
    response = client.post("/predict", json={})
    # Should not crash silently — expecting an error since 'features' key is missing
    assert response.status_code in [400, 500]