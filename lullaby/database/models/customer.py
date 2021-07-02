
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from lullaby.database.models.base import BaseModel


class Customer(BaseModel):
    __tablename__ = 'customer'

    name = Column(String)
    email = Column(String, unique=True)

    favorites = relationship('Favorite', uselist=True, backref='customer')

    def __repr__(self):
        return f'Customer {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
        }
