from yasuo import LolApi
from yasuo.enum import Regions
from examples.examples_config import summoner_name, region

def summoner_by_id(apikey: str):
  lol_api = LolApi(apikey=apikey)
  summoner = lol_api.summoner.by_name(summoner_name, region)
  return lol_api.summoner.by_id(summoner.id, region)
