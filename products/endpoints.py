# products/endpoint.py
from flask import request, jsonify
from flask_restx import Resource, Namespace
from pydantic import ValidationError

from .models import product_post_model, product_patch_model, Product, ProductPatch
from .utils import load_products, save_products


def product_namespace(api):
    ns = Namespace('products', description='Product operations')
    product_post_swagger_model = product_post_model(api)
    product_patch_swagger_model = product_patch_model(api)

    @ns.route('/')
    class ProductList(Resource):
        def get(self):
            products = load_products()
            return jsonify([product.dict() for product in products])

        @ns.expect(product_post_swagger_model)
        def post(self):
            try:
                product_data = Product(**request.json)
            except ValidationError as e:
                return {"errors": e.errors()}, 400

            products = load_products()
            product_data.id = (max([product.id for product in products], default=0) + 1
                               if products else 1)  # Assign a new ID by finding the max ID in database
            products.append(product_data)
            save_products(products)

            return product_data.model_dump_json(), 201

    @ns.route('/<int:id>')
    @ns.response(404, 'Product not found')
    class ProductItem(Resource):
        @ns.expect(product_patch_swagger_model)
        def patch(self, id):
            products = load_products()
            product = next((p for p in products if p.id == id), None)

            if not product:
                ns.abort(404, "Product not found")

            try:
                update_data = ProductPatch(**request.json)
            except ValidationError as e:
                return {"errors": e.errors()}, 400

            # Update only the fields present in update_data
            for field, value in update_data.model_dump(exclude_unset=True).items():
                if value is not None:
                    setattr(product, field, value)

            save_products(products)
            return product.model_dump_json(), 201

    return ns
