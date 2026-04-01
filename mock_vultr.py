from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v2/account', methods=['GET'])
def get_account():
    # Fake account info
    return jsonify({
        "account": {
            "balance": -50.00,
            "pending_charges": 0.00,
            "last_payment_date": "2026-03-30",
            "email": "ahmadch5360@gmail.com"
        }
    })

@app.route('/v2/instances', methods=['POST'])
def create_instance():
    # Fake server creation
    return jsonify({
        "instance": {
            "id": "mock-id-999",
            "os": "Ubuntu 22.04",
            "ram": 2048,
            "status": "pending",
            "main_ip": "192.168.1.100"
        }
    }), 202

if __name__ == '__main__':
    print("Mock Vultr API is running on http://127.0.0.1:5000")
    app.run(port=5000)