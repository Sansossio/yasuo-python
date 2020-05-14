from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.match_list import MatchlistDto

class MatchApi(BaseApi):
  "Match api"
  __base_path = "match/v4"

  def list_by_summoner (self, summoner_id: str, region: Regions):
    "Get match list by summoner id"
    path = self.__base_path + "/matchlists/by-account/" + summoner_id
    response = self.request(
      path=path,
      region=region
    )
    return MatchlistDto.create(response)
