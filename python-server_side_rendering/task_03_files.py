from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])  # Convert price to float
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    
    if product_id is not None:
        products = [p for p in data if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
    else:
        products = data
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
