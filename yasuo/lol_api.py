from .apis.lol import SummonerApi

# League of legends api
class LolApi:
  """
    League of legends api methods
  """
  summoner: SummonerApi
  __apikey: str

  def __init__(self, apikey: str):
    self.__apikey = apikey
    self.__initApis()
  # Initialize apis
  def __initApis(self):
    self.summoner = SummonerApi(self.__apikey)
