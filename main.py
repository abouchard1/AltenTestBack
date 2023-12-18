from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from products.endpoints import product_namespace

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_namespace(product_namespace(api))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
