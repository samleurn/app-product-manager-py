from flask import Flask, request, jsonify
from db import DB

# from app.db.database import Query

app = Flask(__name__)


@app.route("/api/health")
def health():
    return "Ok"


@app.route("/api/")
def home():
    return "Welcome to the Product Manager API"


@app.route("/api/brand", methods=["POST"])
def post_brand():
    data = request.get_json()

    name = data["name"]
    cnpj = data["cnpj"]

    query = """INSERT INTO stock (name, cnpj) VALUES (%s, %s)"""

    DB(query, (name, cnpj)).query()

    return jsonify({"msg": f"{data['name']} pushed"})


@app.route("/api/product", methods=["POST"])
def post_product():

    return {"status": 201, "msg": "Product Pushed"}


@app.route("/api/batch", methods=["POST"])
def post_batch():
    return {"status": 201, "msg": "Batch Pushed"}


if __name__ == "__main__":
    app.run(debug=True)
