import requests
import yasuo.config as config
from yasuo.errors import ApikeyNotFound
from yasuo.enum import Regions
from yasuo.apis.utils import api_error_handler

# Base api
class BaseApi:
  __apikey: str

  def __init__(self, apikey: str):
    if not apikey:
      raise ApikeyNotFound()
    self.__apikey = apikey

  def __parseUrl(self, region: Regions, path: str):
    url = config.BASE_URL.replace("LOL_REGION", region.value)
    url += "/" + path
    return url

  def request(self, region: Regions, path: str):
    response = requests.get(
      url=self.__parseUrl(region, path),
      headers={
        "X-Riot-Token": self.__apikey
      }
    )
    api_error_handler(response)
    return response.json()
