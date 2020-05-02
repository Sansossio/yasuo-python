from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.champion import ChampionInfoDTO

class ChampionApi(BaseApi):
  "Champion api"
  __base_path = "platform/v3/champion-rotations"

  def free_champs (self, region: Regions):
    "Get free champs"
    response = self.request(
      path=self.__base_path,
      region=region
    )
    return ChampionInfoDTO.create(response)
