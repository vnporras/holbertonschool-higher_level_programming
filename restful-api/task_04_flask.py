#!/usr/bin/python3
from flask import Flask, jsonify, request


users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users_name():
    usernames = list(users.keys())
    if not usernames:
        return jsonify({'message': 'Users not found'}), 404
    return jsonify(usernames)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/add_user', methods=['POST'])
def add_user():

    data = request.json
    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if username is None or username == '':
        return jsonify({'error': 'Username Required'}), 400

    if username in users:
        return jsonify({'error': 'Username already exists. Choose a different username.'}), 400

    new_user = {
        'username': username,
        'name': name,
        'age': age,
        'city': city
    }

    users[username] = new_user

    return jsonify({'message': 'User added', 'user': new_user}), 201

if __name__ == "__main__":
    app.run()