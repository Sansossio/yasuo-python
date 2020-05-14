from yasuo import LolApi
from yasuo.enum import Regions
from examples.examples_config import summoner_name, region

def matchlist_by_summoner_id(apikey: str):
  lol_api = LolApi(apikey=apikey)
  summoner = lol_api.summoner.by_name(summoner_name, region)
  return lol_api.match.list_by_summoner(summoner.account_id, region)
