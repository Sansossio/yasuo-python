from .apis.lol import *

# League of legends api
class LolApi:
  """
    League of legends api methods
  """
  # Apis
  summoner: SummonerApi
  champion: ChampionApi
  champion_mastery: ChampionMasteryApi
  league: LeagueApi
  league_exp: LeagueExpApi
  status: StatusApi

  # Internal properties
  __apikey: str

  def __init__(self, apikey: str):
    self.__apikey = apikey
    self.__initApis()
  # Initialize apis
  def __initApis(self):
    self.summoner = SummonerApi(self.__apikey)
    self.champion = ChampionApi(self.__apikey)
    self.champion_mastery = ChampionMasteryApi(self.__apikey)
    self.league = LeagueApi(self.__apikey)
    self.status = StatusApi(self.__apikey)
    self.league_exp = LeagueExpApi(self.__apikey)
