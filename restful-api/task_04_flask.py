#!/opt/homebrew/bin/python3
from flask import Flask, jsonify, request


users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users_name():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"User not found"})

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')

    if username in users:
        return jsonify({"User already exists"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"user": "User added successfully", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
