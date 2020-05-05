from yasuo import LolApi
from yasuo.enum import Regions
from examples.examples_config import summoner_name, region

def summoner_by_name(apikey: str):
  lol_api = LolApi(apikey=apikey)
  return lol_api.summoner.by_name(summoner_name, Regions.KOREA)
