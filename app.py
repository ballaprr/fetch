from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import uuid
from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///processor.db'
db = SQLAlchemy(app)
api = Api(app)

# Database:
# Receipt table: id (char(200)), retailer (char(100)), purchaseDate (Date), purchaseTime(Time), total(float)
# Item table: id (int), shortDescription (char(200)), price(float)
class Receipt(db.Model):
    id = db.Column(db.String(length=50), primary_key=True)
    retailer = db.Column(db.String(length=200), nullable=False)
    purchaseDate = db.Column(db.DateTime(), nullable=False)
    purchaseTime = db.Column(db.Time(), nullable=False)
    total = db.Column(db.Float(), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receipt_id = db.Column(db.String(50), db.ForeignKey('receipt.id'), nullable=False)
    description = db.Column(db.String(length=200), nullable=False)
    price = db.Column(db.Float(), nullable=False, unique=False)


# post request: pass in receipt json and store in recept and item table, generate id and store, response should be the id

@app.route('/receipts/process', methods=['POST'])
def process():
    data = request.get_json()

    receipt_id = str(uuid.uuid4())

    receipt = Receipt(id=receipt_id, retailer=data['retailer'], purchaseDate=datetime.strptime(data['purchaseDate'], '%Y-%m-%d'), purchaseTime=datetime.strptime(data['purchaseTime'], '%H:%M').time(), total=data['total'])

    db.session.add(receipt)

    for item in data.get('items', []):
        db.session.add(Item(receipt_id=receipt_id, description=item['shortDescription'], price=item['price']))

    db.session.commit()
    return jsonify({"id": receipt_id}), 201


# get request: pass in id to path and using criteria compute the points and return

@app.route('/receipts/<string:receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    receipt = db.session.get(Receipt, receipt_id)
    points = 0
    if not receipt:
        return {"error": "Receipt not found"}, 404
    # 1 pointer for every alphanumeric character in the retailer name
    logger.info('test')
    logger.info('test docker compose')

    # 50 points if total is round dollar amount with no cents

    # 25 points if total is multiple of .25

    # 5 points for every two items in the receipt

    # trimmed length of item multiple of 3, * 0.2 round 
    
    return jsonify({
        "id": receipt.id
    })
    
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
