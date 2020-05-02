from yasuo.errors.apikey_not_found import ApikeyNotFound
# Api api
class BaseApi:
  __apikey: str

  def __init__(self, apikey: str):
    if not apikey:
      raise ApikeyNotFound()
    self.__apikey = apikey
