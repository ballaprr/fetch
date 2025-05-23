import sys
sys.path.append('/app')

from app import app

def test_receiptprocess():
    with app.test_client() as c:
        response = c.post('/receipts/process', json={
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            }
        ],
        "total": "9.00"
        })
        assert response.status_code == 201
        json_response = response.get_json()
        assert 'id' in json_response
        assert isinstance(json_response['id'], str)

        get_response = c.get(f"/receipts/{json_response['id']}/points")
        assert get_response.status_code == 200
        json_response = get_response.get_json()
        assert json_response['points'] == 109

def test_receiptprocess1():
    with app.test_client() as c:
        response = c.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
        })
        assert response.status_code == 201
        json_response = response.get_json()
        assert 'id' in json_response
        assert isinstance(json_response['id'], str)

        get_response = c.get(f"/receipts/{json_response['id']}/points")
        assert get_response.status_code == 200
        json_response = get_response.get_json()
        assert json_response['points'] == 28

def test_wrongitemprocess():
    with app.test_client() as c:
        response = c.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
        })
        assert response.status_code == 400
        json_response = response.get_json()
        assert isinstance("Invalid Item input", str)

def test_wrongreceiptprocess():
    with app.test_client() as c:
        response = c.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
        })
        assert response.status_code == 400
        json_response = response.get_json()
        assert isinstance("Invalid Item input", str)

def test_points():
    with app.test_client() as c:
        response = c.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
        })
        assert response.status_code == 201
        json_response = response.get_json()
        assert 'id' in json_response
        assert isinstance(json_response['id'], str)

        get_response = c.get(f"/receipts/'check/points")
        assert get_response.status_code == 404
        json_response = get_response.get_json()
        assert isinstance("Receipt not found", str)