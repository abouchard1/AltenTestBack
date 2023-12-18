# products/model.py
from typing import Optional

from flask_restx import fields
from pydantic import BaseModel


def product_post_model(api):
    return api.model('Post Product', {
        'code': fields.String(required=True, description='Product code'),
        'name': fields.String(required=True, description='Product name'),
        'description': fields.String(required=True, description='Product description'),
        'image': fields.String(description='Product image URL'),
        'price': fields.Float(required=True, description='Product price'),
        'category': fields.String(required=True, description='Product category'),
        'quantity': fields.Integer(required=True, description='Quantity in stock'),
        'inventoryStatus': fields.String(required=True, description='Inventory status'),
        'rating': fields.Float(description='Product rating')
    })


def product_patch_model(api):
    return api.model('Patch Product', {
        'code': fields.String(description='Product code'),
        'name': fields.String(description='Product name'),
        'description': fields.String(description='Product description'),
        'image': fields.String(description='Product image URL'),
        'price': fields.Float(description='Product price'),
        'category': fields.String(description='Product category'),
        'quantity': fields.Integer(description='Quantity in stock'),
        'inventoryStatus': fields.String(description='Inventory status'),
        'rating': fields.Float(description='Product rating')
    })


class Product(BaseModel):
    id: Optional[int] = None
    code: str
    name: str
    description: str
    price: float
    quantity: int
    inventoryStatus: str
    category: str
    image: Optional[str] = None
    rating: Optional[float] = None


class ProductPatch(BaseModel):
    id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    inventoryStatus: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None
    rating: Optional[float] = None
