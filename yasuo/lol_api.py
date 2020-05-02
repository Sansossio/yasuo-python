from yasuo.apis.lol.summoner_api import SummonerApi

# League of legends api
class LolApi:
  summoner: SummonerApi
  __apikey: str
  """
    Apikey = Riot apikey
  """
  def __init__(self, apikey: str):
    self.__apikey = apikey
    self.__initApis()
  # Initialize apis
  def __initApis(self):
    self.summoner = SummonerApi(self.__apikey)
