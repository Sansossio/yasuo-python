from yasuo import LolApi
from yasuo.enum import Regions
from examples.examples_config import summoner_name, region

def champion_mastery_summoner_score(apikey: str):
  lol_api = LolApi(apikey=apikey)
  summoner = lol_api.summoner.by_name(summoner_name, region)
  return lol_api.champion_mastery.summoner_score(summoner.id, region)
