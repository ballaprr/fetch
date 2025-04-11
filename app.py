from flask import Flask
import sqlite3
import os

app = Flask(__name__)

conn = sqlite3.connect('database.db')
# Database:
# Receipt table: id (char(200)), relatiler (char(100)), purchaseDate (Date), purchaseTime(Time), total(float)
# Item table: id (int), shortDescription (char(200)), price(float)


# post request: pass in receipt json and store in recept and item table, generate id and store, response should be the id

# get request: pass in id to path and using criteria compute the points and return

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
