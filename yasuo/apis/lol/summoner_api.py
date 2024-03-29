from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.summoner import SummonerDTO

class SummonerApi(BaseApi):
  "Summoner api"
  __base_path = "summoner/v4/summoners"

  def by_name (self, summoner_name: str, region: Regions):
    "Get a summoner by summoner name."
    path = self.__base_path + "/by-name/" + summoner_name
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)

  def by_id (self, id: str, region: Regions):
    "Get a summoner by summoner ID."
    path = self.__base_path + "/" + id
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)

  def by_puuid (self, puuid: str, region: Regions):
    "Get a summoner by PUUID."
    path = self.__base_path + "/by-puuid/" + puuid
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)

  def by_account (self, account: str, region: Regions):
    "Get a summoner by account ID."
    path = self.__base_path + "/by-account/" + account
    response = self.request(
      path=path,
      region=region
    )
    return SummonerDTO.create(response)
