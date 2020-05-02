from yasuo import LolApi
from yasuo.enum import Regions

def summoner_by_name(apikey: str):
  lol_api = LolApi(apikey=apikey)
  name = "Hide on Bush"
  summoner = lol_api.summoner.by_name(summoner_name=name, region=Regions.KOREA)
  return summoner
