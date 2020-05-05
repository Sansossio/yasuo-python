from yasuo import LolApi
from examples.examples_config import summoner_name, region, queue

def master_league_by_queue(apikey: str):
  lol_api = LolApi(apikey=apikey)
  return lol_api.league.master_leagues_by_queue(queue, region)
