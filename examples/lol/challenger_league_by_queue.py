from yasuo import LolApi
from examples.examples_config import summoner_name, region, queue

def challenger_league_by_queue(apikey: str):
  lol_api = LolApi(apikey=apikey)
  return lol_api.league.challenger_leagues_by_queue(queue, region)
