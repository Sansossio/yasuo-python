from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.champion_mastery import ChampionMasteryDTO

class ChampionMasteryApi(BaseApi):
  "Champion mastery api"
  __base_path = "champion-mastery/v4/champion-masteries/by-summoner"

  def by_summoner (self, summoner_id: str, region: Regions):
    "Get summoner champions masteries"
    path = self.__base_path + "/" + summoner_id
    response = self.request(
      path=path,
      region=region
    )
    return list(map(ChampionMasteryDTO.create, response))
