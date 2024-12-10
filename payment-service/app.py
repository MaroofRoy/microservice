#Maroof-k237703
#from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)
@app.route('/pay', methods=['POST'])
@swag_from('swagger/register.yml')
def pay():
    data = request.json
    if data['amount'] > 0:
        return jsonify({"message": "Payment successful"}), 200
    return jsonify({"message": "Payment failed"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)

