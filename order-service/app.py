from flask import Flask, request, jsonify
import requests
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

@app.route('/place-order', methods=['POST'])
@swag_from('swagger/register.yml')
def place_order():
    data = request.json
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    
    # Call Product-Service to check inventory
    product_service_url = "http://product-service:5002/check-inventory"
    response = requests.post(product_service_url, json={"product_id": product_id, "quantity": quantity})
    
    if response.status_code == 200:
        # Inventory check passed; process order
        return jsonify({"message": "Order placed successfully!"}), 200
    else:
        # Inventory check failed
        return jsonify({"error": response.json()}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
