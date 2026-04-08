from flask import Flask, jsonify
from flask_cors import CORS  # <--- Add this

app = Flask(_name_)
CORS(app)  # <--- Add this to allow the frontend to connect

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ])

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
