import json

import requests

from lullaby.exceptions import IntegtarionError
from lullaby.settings import PRODUCT_URI


def get_product(product_id):
    """
    Função responsável por buscar na API de produto, seus detalhes
    :param product_id: Identificador único de produto
    :return: Detalhes do produto
    """
    request_url = f"{PRODUCT_URI}/{product_id}/"

    headers = {
        "Content-Type": "application/json",
        "Accept":  "application/json"
    }
    try:
        response = requests.get(request_url, headers=headers)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    if response.status_code == 200:
        return json.loads(response.content)

    raise IntegtarionError()
