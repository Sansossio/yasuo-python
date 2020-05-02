from http import HTTPStatus
from yasuo.errors.invalid_apikey import InvalidApikey

def api_error_handler (response):
  if response.status_code == HTTPStatus.FORBIDDEN:
      raise InvalidApikey()
