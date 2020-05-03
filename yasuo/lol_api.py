from .apis.lol import SummonerApi, ChampionApi, ChampionMasteryApi

# League of legends api
class LolApi:
  """
    League of legends api methods
  """
  # Apis
  summoner: SummonerApi
  champion: ChampionApi
  champion_mastery: ChampionMasteryApi

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
