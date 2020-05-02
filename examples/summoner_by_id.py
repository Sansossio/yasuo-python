from yasuo import LolApi
from yasuo.enum import Regions

def summoner_by_id(apikey: str):
  lol_api = LolApi(apikey=apikey)
  name = "Hide on Bush"
  region = Regions.KOREA
  summoner = lol_api.summoner.by_name(summoner_name=name, region=region)
  return lol_api.summoner.by_id(id=summoner.id, region=region)
