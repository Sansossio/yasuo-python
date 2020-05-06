from yasuo import LolApi
from yasuo.enum import Divisions, ExpTiers
from examples.examples_config import summoner_name, region, queue

def league_exp_entries(apikey: str):
  lol_api = LolApi(apikey=apikey)
  page = 1 # optional param
  return lol_api.league_exp.get_entries(queue, ExpTiers.CHALLENGER, Divisions.I, region, page)
