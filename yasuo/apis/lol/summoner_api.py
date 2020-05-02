from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.summoner.summoner_dto import SummonerDTO

class SummonerApi(BaseApi):
  "Summoner api"
  __base_path = "summoner/v4/summoners"

  def by_name (self, summoner_name: str, region: Regions):
    "Get summoner by name"
    path = self.__base_path + "/by-name/" + summoner_name
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)

  def by_id (self, id: str, region: Regions):
    "Get summoner by id"
    path = self.__base_path + "/" + id
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)
