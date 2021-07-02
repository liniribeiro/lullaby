from sqlalchemy.exc import IntegrityError

from lullaby.database.queries import get_favorites_by_customer_id, get_favorite_product, \
    save_favorite
from lullaby.exceptions import DuplicatedProductError, FavoriteNotFoundError
from lullaby.helpers.redis import get_from_cache, add_to_cache
from lullaby.schemas.customer_schema import FavoriteModel, FavoriteList
from lullaby.talkers.products import get_product


def get_customer_favorites(customer_id):
    """
    Responsável por retornar uma lista de todos os favoritos do consumidor.
    :param customer_id: identificador único do consumidor
    :return: Lista de favoritos.
    """
    favorites = get_favorites_by_customer_id(customer_id)
    favorites = [get_product_details(favorite['product_id']) for favorite in favorites]
    favorite_list = FavoriteList()
    favorite_list.favorites = favorites
    return favorite_list


def get_product_details(product_id):
    """
    função responsavél pelos detalhes de um produto. Se não encontra o emsmo em cache, busca na API de produtos.
    :param product_id: Identificador único do produto
    :return: Objeto com os dados de produto favorito.
    """
    product = get_from_cache(product_id)
    if product is None:
        product = get_product(product_id)
        add_to_cache(product_id, product)
    return FavoriteModel(product, strict=False)


def add_favorite(data, customer_id):
    """
    Função responsável por adicionar um novo favorito ao consumidor.
    """
    try:
        save_favorite(customer_id, data['product_id'])
    except IntegrityError as e:
        raise DuplicatedProductError()


def get_favorite_product_by_id(customer_id, product_id):
    try:
        return get_favorite_product(customer_id, product_id)
    except Exception as e:
        raise FavoriteNotFoundError()


def get_favorite(customer_id, product_id):
    favorite_product = get_favorite_product_by_id(customer_id, product_id)
    return get_product_details(favorite_product['product_id'])



