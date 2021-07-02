from typing import Text

from sqlalchemy import text, exists

from lullaby.database.db_connection import DBConnector
from lullaby.database.models import Favorite, Customer


def save(db_model, dict_object):
    with DBConnector().conn_session() as session:
        object_class = db_model(**dict_object)
        session.add(object_class)
        session.flush()
        return str(object_class.id)


def get_all(db_model):
    with DBConnector().conn_session() as session:
        db_object = session.query(db_model).all()
        return [c.to_dict() for c in db_object]


def get_by_id(db_model, object_id: Text):
    with DBConnector().conn_session() as session:
        db_object = session.query(db_model).filter_by(id=object_id).first()
        return db_object.to_dict()


def delete_customer(object_id):
    with DBConnector().conn_session() as session:
        session.query(Customer).filter_by(id=object_id).delete()


def update_customer(customer_id, customer_name=None, customer_email=None):
    with DBConnector().conn_session() as session:
        customer_model = session.query(Customer).filter_by(id=customer_id).first()
        customer_model.name = customer_name if customer_name else customer_model.name
        customer_model.email = customer_email if customer_email else customer_model.email
        session.add(customer_model)


def customer_exists(customer_id):
    with DBConnector().conn_session() as session:
        return session.query(exists().where(Customer.id == customer_id)).scalar()


def delete_favorite(customer_id, product_id):
    with DBConnector().conn_session() as session:
        return session.query(Favorite).filter_by(customer_id=customer_id, product_id=product_id).delete()


def get_favorite_product(customer_id, product_id):
    with DBConnector().conn_session() as session:
        favorite = session.query(Favorite).filter_by(customer_id=customer_id, product_id=product_id).first()
        return favorite.to_dict()


def save_favorite(customer_id, product_id):
    with DBConnector().conn_session() as session:
        favorite = Favorite()
        favorite.product_id = product_id
        favorite.customer_id = customer_id
        session.add(favorite)
        session.flush()


def get_favorites_by_customer_id(customer_id):
    with DBConnector().conn_session() as session:
        favorites = session.query(Favorite).filter_by(customer_id=customer_id).all()
        return [favorite.to_dict() for favorite in favorites]
