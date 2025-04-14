# Fetch Assessment

## Technology
Python 3.9.0
- Flask
- Flask REST
- SQLite
- Docker


## Prerequisites
- Ensure Docker is Installed

## Running

Build the image
```bash
docker-compose build
```

To run the application

This will also create the SQLite database after the first query:
```bash
docker-compose up
```
Run only the web service
```bash
docker-compose run web
```

Run only the test service
```bash
docker-compose run test
```

## Testing

Open Postman or curl

Execute the following Post request
```bash
curl -X POST http://localhost:5000/receipts \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

Add the following Get request
```bash
curl http://localhost:5000/receipts/<process_id>/points
```
