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

    if not data or not data.get('username') or not data.get('name') or not data.get('age') or not data.get('city'):
        return jsonify({'error': 'All fields (username, name, age, city) are required.'}), 400

    username = data.get('username')

    if username == '':
        return jsonify({'error': 'Username cannot be empty.'}), 400

    if username in users:
        return jsonify({'error': 'Username already exists. Choose a different username.'}), 400

    new_user = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }

    users[username] = new_user

    return jsonify({'message': 'User added', 'user': new_user}), 201


if __name__ == "__main__":
    app.run()