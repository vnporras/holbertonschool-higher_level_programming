from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_data_from_json():
    with open('products.json') as f:
        data = json.load(f)
    return data['items']

def get_data_from_csv():
    items = []
    with open('products.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items

def get_data_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    items = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in items]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []

    if source == 'json':
        data = get_data_from_json()
    elif source == 'csv':
        data = get_data_from_csv()
    elif source == 'sql':
        data = get_data_from_sql()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        product_id = int(product_id)
        data = [item for item in data if item['id'] == product_id]
        if not data:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', items=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
