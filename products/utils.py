# products/utils.py
import json
from typing import List

from products.models import Product

JSON_FILE = 'products/products.json'


def load_products() -> List[Product]:
    try:
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
            return [Product(**item) for item in data.get('data', [])]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_products(products: List[Product]):
    with open(JSON_FILE, 'w') as file:
        json.dump({"data": [product.dict() for product in products]}, file, indent=4)
