from .apis.lol import SummonerApi, ChampionApi

# League of legends api
class LolApi:
  """
    League of legends api methods
  """
  summoner: SummonerApi
  champion: ChampionApi
  __apikey: str

  def __init__(self, apikey: str):
    self.__apikey = apikey
    self.__initApis()
  # Initialize apis
  def __initApis(self):
    self.summoner = SummonerApi(self.__apikey)
    self.champion = ChampionApi(self.__apikey)
