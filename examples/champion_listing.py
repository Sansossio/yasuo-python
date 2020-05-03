from yasuo import LolApi
from examples.examples_config import summoner_name, region

def champion_listing(apikey: str):
  lol_api = LolApi(apikey=apikey)
  return lol_api.champion.champion_listing()
