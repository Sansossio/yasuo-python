from yasuo import LolApi
from examples.examples_config import summoner_name, region

def champion_free_rotation(apikey: str):
  lol_api = LolApi(apikey=apikey)
  return lol_api.champion.free_champs(region)
