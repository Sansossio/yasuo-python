from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.summoner.summoner_dto import SummonerDTO

# Summoner api
class SummonerApi(BaseApi):
  __base_path = "summoner/v4/summoners"
  # Get summoner by name
  def by_name (self, summoner_name: str, region: Regions) -> SummonerDTO:
    path = self.__base_path + "/by-name/" + summoner_name
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)
