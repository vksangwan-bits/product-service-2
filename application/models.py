# application/models.py
from . import db
from datetime import datetime, timezone


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), unique=False, nullable=True)
    date_added = db.Column(db.DateTime, default=str(datetime.now(timezone.utc)))
    date_updated = db.Column(db.DateTime, onupdate=str(datetime.now(timezone.utc)))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'price': self.price,
            'image': self.image
        }
