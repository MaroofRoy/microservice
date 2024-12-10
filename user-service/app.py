#from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

users = {}  # In-memory storage for simplicity

@app.route('/register', methods=['POST'])
@swag_from('swagger/register.yml')
def register():
    data = request.json
    if data['username'] in users:
        return jsonify({"message": "User already exists"}), 400
    users[data['username']] = data['password']
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if users.get(data['username']) == data['password']:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
