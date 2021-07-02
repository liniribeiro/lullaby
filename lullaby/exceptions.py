from http import HTTPStatus


class Error(Exception):
    data = {}
    name = None
    status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.data = kwargs.get("data")
        self.name = kwargs.get("name")
        self.name = kwargs.get("status")


class AuthenticationError(Error):
    def __str__(self):
        return "not-authorized"


class PayloadError(Error):
    def __str__(self):
        return "payload-error"


class DuplicatedEmailError(Error):
    def __str__(self):
        return "email-already-used"


class CustomerNotFoundError(Error):
    def __str__(self):
        return "customer-not-found"


class DuplicatedProductError(Error):
    def __str__(self):
        return "duplicated-list-product"


class FavoriteNotFoundError(Error):
    def __str__(self):
        return "favorite-not-found"


class IntegtarionError(Error):
    def __str__(self):
        return "product-integration-error"


class NotAuthorizedError(Error):
    def __str__(self):
        return "not-authorized-error"
