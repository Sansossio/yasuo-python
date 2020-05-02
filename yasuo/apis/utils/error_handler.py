from http import HTTPStatus
from yasuo.errors import InvalidApikey, NotFoundException

def api_error_handler (response):
  status_code = response.status_code
  if status_code == HTTPStatus.FORBIDDEN:
    raise InvalidApikey()
  if status_code == HTTPStatus.NOT_FOUND:
    raise NotFoundException()
