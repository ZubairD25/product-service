# AI Disclosure:
# ChatGPT was used to assist with understanding REST API concepts and implementing the task endpoints.
# All code was reviewed, tested, and understood before submission.


from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

#replacing WRAP to Flask
app = Flask(__name__)
CORS(app)



@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]

    return jsonify(products)

#Factor 7
if __name__ == "__main__":
    port = int(os.getenv("PORT", 3030))
    app.run(host="0.0.0.0", port=port)

