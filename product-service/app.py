#Maroof-k237703
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)
# Dummy inventory data
inventory = {"1": 10, "2": 5, "3": 0}

@app.route('/check-inventory', methods=['POST'])
@swag_from('swagger/register.yml')
def check_inventory():
    data = request.json
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    
    if product_id in inventory and inventory[product_id] >= quantity:
        # Reduce stock and confirm
        inventory[product_id] -= quantity
        return jsonify({"message": "Inventory check passed"}), 200
    else:
        # Inventory insufficient
        return jsonify({"error": "Insufficient inventory"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

