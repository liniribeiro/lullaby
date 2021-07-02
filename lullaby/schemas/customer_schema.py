
from schematics import Model
from schematics.types import StringType, ListType, ModelType, EmailType, FloatType, UUIDType


class SaveCustomerInput(Model):
    email = EmailType()
    name = StringType()


class CustomerSchemaModel(Model):
    id = UUIDType()
    name = StringType()
    email = StringType()


class CustomerOutputList(Model):
    customers = ListType(ModelType(CustomerSchemaModel))


class SaveFavoriteInput(Model):
    customer_id = UUIDType()
    product_id = UUIDType()


class FavoriteModel(Model):
    id = StringType()
    title = StringType()
    image = StringType()
    price = FloatType()
    reviewScore = FloatType()


class FavoriteList(Model):
    favorites = ListType(ModelType(FavoriteModel))
