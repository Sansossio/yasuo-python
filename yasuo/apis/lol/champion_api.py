from typing import List
from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.champion import ChampionFreeRotationDTO, ChampionDTO

class ChampionApi(BaseApi):
  "Champion api"
  __base_path = "platform/v3/champion-rotations"
  __champions_url = "http://ddragon.leagueoflegends.com/cdn/10.9.1/data/"

  def __get_champion_id(self, data):
    return data["id"]

  def free_champs(self, region: Regions):
    "Get free champs"
    response = self.request(
      path=self.__base_path,
      region=region
    )
    return ChampionFreeRotationDTO.create(response)

  def champion_details(self, name: str, lang: str = "en_US"):
    url = self.__champions_url + lang + "/champion/" + name + ".json"
    champion = self.requestService.get(url).json()
    return ChampionDTO.create(champion)

  def champion_listing(self, lang = "en_US"):
    url = self.__champions_url + lang + "/champion.json"
    data = self.requestService.get(url).json()
    championNames = list(map(self.__get_champion_id, list(data["data"].values())))
    return list(map(self.champion_details, championNames))
