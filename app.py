from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///processor.db'
db = SQLAlchemy(app)

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
    receipt_id = db.Column(db.String(50), db.ForeignKey('receipt.id'), nullable=False)
    description = db.Column(db.String(length=200), nullable=False)
    price = db.Column(db.Float(), nullable=False, unique=False)

# post request: pass in receipt json and store in recept and item table, generate id and store, response should be the id

# get request: pass in id to path and using criteria compute the points and return

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
