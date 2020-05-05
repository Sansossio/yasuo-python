from yasuo.apis.base_api import BaseApi
from yasuo.enum import Regions, Champions
from yasuo.dto.champion_mastery import ChampionMasteryDTO
from typing import List

class ChampionMasteryApi(BaseApi):
  "Champion mastery api"
  __base_path = "champion-mastery/v4/champion-masteries/by-summoner"

  def champion_by_summoner(self, summoner_id: str, champion: Champions, region: Regions):
    "Get all champion mastery entries sorted by number of champion points descending."
    path = self.__base_path + "/" + summoner_id + "/by-champion/" + str(champion.value)
    response = self.request(
      path=path,
      region=region
    )
    return ChampionMasteryDTO.create(response)

  def summoner_score(self, summoner_id: str, region: Regions):
    "Get a player's total champion mastery score, which is the sum of individual champion mastery levels."
    path = "champion-mastery/v4/scores/by-summoner/" + summoner_id
    data: int = self.request(
      path=path,
      region=region
    )
    return data

  def by_summoner (self, summoner_id: str, region: Regions):
    "Get a champion mastery by player ID and champion ID."
    path = self.__base_path + "/" + summoner_id
    data = self.request(
      path=path,
      region=region
    )
    response: List[ChampionMasteryDTO] = list(map(ChampionMasteryDTO.create, data))
    return response
