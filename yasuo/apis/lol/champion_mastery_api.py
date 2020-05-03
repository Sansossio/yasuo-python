from yasuo.apis.base_api import BaseApi
from yasuo.enum import Regions, Champions
from yasuo.dto.champion_mastery import ChampionMasteryDTO
from typing import List

class ChampionMasteryApi(BaseApi):
  "Champion mastery api"
  __base_path = "champion-mastery/v4/champion-masteries/by-summoner"

  def champion_by_summoner(self, summoner_id: str, champion: Champions, region: Regions):
    "Get champion mastery by summoner"
    path = self.__base_path + "/" + summoner_id + "/by-champion/" + str(champion.value)
    response = self.request(
      path=path,
      region=region
    )
    return ChampionMasteryDTO.create(response)

  def by_summoner (self, summoner_id: str, region: Regions) -> List[ChampionMasteryDTO]:
    "Get summoner champions masteries"
    path = self.__base_path + "/" + summoner_id
    data = self.request(
      path=path,
      region=region
    )
    response = map(ChampionMasteryDTO.create, data)
    return list(response)
