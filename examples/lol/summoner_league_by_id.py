from yasuo import LolApi
from yasuo.enum import Regions
from examples.examples_config import summoner_name, region

def summoner_league_by_id(apikey: str):
  lol_api = LolApi(apikey=apikey)
  summoner = lol_api.summoner.by_name(summoner_name, region)
  return lol_api.league.leagues_by_summoner_id(summoner.id, region)
