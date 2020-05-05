from yasuo import LolApi
from examples.examples_config import summoner_name, region, queue

def league_by_league_id(apikey: str):
  lol_api = LolApi(apikey=apikey)
  summoner = lol_api.summoner.by_name(summoner_name, region)
  league = lol_api.league.leagues_by_summoner_id(summoner.id, region)[0].league_id
  return lol_api.league.by_league_id(league, region)
  
