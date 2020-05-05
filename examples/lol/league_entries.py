from yasuo import LolApi
from examples.examples_config import summoner_name, region, queue, tier, division

def league_entries(apikey: str):
  lol_api = LolApi(apikey=apikey)
  page = 1 # optional param
  return lol_api.league.get_entries(queue, tier, division, region, page)
