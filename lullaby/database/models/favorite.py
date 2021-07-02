from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from lullaby.database.models.base import BaseModel


class Favorite(BaseModel):
    __tablename__ = 'favorite'
    __table_args__ = (UniqueConstraint('product_id', 'customer_id', name='favorite1')),

    product_id = Column(String)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return f'Customer {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'product_id': self.product_id,
            'customer_id': self.customer_id,
        }
