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