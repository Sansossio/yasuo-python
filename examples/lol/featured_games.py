from yasuo import LolApi
from examples.examples_config import summoner_name, region

def featured_games(apikey: str):
  lol_api = LolApi(apikey=apikey)
  return lol_api.spectator.featured_games(region)
