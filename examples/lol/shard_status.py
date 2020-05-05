from yasuo import LolApi
from examples.examples_config import  region

def shard_status(apikey: str):
  lol_api = LolApi(apikey=apikey)
  response = lol_api.status.shard_status(region)
  return response
