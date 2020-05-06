from typing import List
from yasuo.apis.base_api import BaseApi
from yasuo.enum import Regions, Queues, ExpTiers, Divisions
from yasuo.dto.league import LeagueListDTO, LeagueItemDTO, LeagueEntryDTO

class LeagueExpApi(BaseApi):
  "Leagues experimental api"
  __base_path = "league-exp/v4"

  @staticmethod
  def __validate_tier_division(tier: ExpTiers, division: Divisions):
    "Validate tier + division"
    if (tier != ExpTiers.CHALLENGER and tier != ExpTiers.GRANDMASTER and tier != ExpTiers.MASTER):
      return

    if (division != Divisions.I):
      raise Exception("Invalid division for tier " + tier.value)

  def get_entries(self, queue: Queues, tier: ExpTiers, division: Divisions, region: Regions, page: int = 1):
    "Get league entries filtering by queue, tier and divison"
    LeagueExpApi.__validate_tier_division(tier, division)
    path = self.__base_path + "/entries/" + queue.value + "/" + tier.value + "/" + division.value
    params = {
      "page": page
    }
    data = self.request(region, path, params)
    response: List[LeagueEntryDTO] = list(map(LeagueEntryDTO.create, data))
    return response

