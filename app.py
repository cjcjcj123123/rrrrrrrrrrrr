from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime


app = Flask(__name__)

# Function to fetch data from API
def fetch_data(year, month, day, price_class):
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None




@app.route('/api/data', methods=['GET'])
def get_data():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    price_class = request.args.get('price_class')

    data = fetch_data(year, month, day, price_class)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Data not found"}), 404

# Index page route
@app.route('/')
def index():
    return render_template('index.html')

# Price class page routes
@app.route('/SE1')
def SE1():
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')

    data = fetch_data(year, month, day, "SE1")
    return render_template('page1.html', data=data)


@app.route('/SE2')
def SE2():
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')

    data = fetch_data(year, month, day, "SE2")
    return render_template('page1.html', data=data)


@app.route('/SE3')
def SE3():
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')

    data = fetch_data(year, month, day, "SE4")
    return render_template('page1.html', data=data)


@app.route('/SE4')
def SE4():
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')

    data = fetch_data(year, month, day, "SE4")
    return render_template('page1.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
