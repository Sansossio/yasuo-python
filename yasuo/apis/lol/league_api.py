from typing import List
from yasuo.apis.base_api import BaseApi
from yasuo.enum import Regions, Queues, Tiers, Divisions
from yasuo.dto.league import LeagueListDTO, LeagueItemDTO, LeagueEntryDTO

class LeagueApi(BaseApi):
  "Leagues api"
  __base_path = "league/v4"

  def challenger_leagues_by_queue(self, queue: Queues, region: Regions):
    "Get the challenger league for given queue."
    path = self.__base_path + "/challengerleagues/by-queue/" + queue.value
    data = self.request(region, path)
    return LeagueListDTO.create(data)

  def leagues_by_summoner_id(self, summoner_id: str, region: Regions):
    "Get league entries in all queues for a given summoner ID."
    path = self.__base_path + "/entries/by-summoner/" + summoner_id
    data = self.request(region, path)
    response: List[LeagueEntryDTO] = list(map(LeagueEntryDTO.create, data))
    return response

  def get_entries(self, queue: Queues, tier: Tiers, division: Divisions, region: Regions, page: int = 1):
    "Get league entries filtering by queue, tier and divison"
    path = self.__base_path + "/entries/" + queue.value + "/" + tier.value + "/" + division.value
    params = {
      "page": page
    }
    data = self.request(region, path, params)
    response: List[LeagueEntryDTO] = list(map(LeagueEntryDTO.create, data))
    return response

  def grandmaster_leagues_by_queue(self, queue: Queues, region: Regions):
    "Get the grandmaster league of a specific queue."
    path = self.__base_path + "/grandmasterleagues/by-queue/" + queue.value
    data = self.request(region, path)
    return LeagueListDTO.create(data)

  def by_league_id(self, league_id: str, region: Regions):
    "Get league with given ID, including inactive entries."
    path = self.__base_path + "/leagues/" + league_id
    data = self.request(region, path)
    return LeagueListDTO.create(data)

  def master_leagues_by_queue(self, queue: Queues, region: Regions):
    "Get the master league for given queue."
    path = self.__base_path + "/masterleagues/by-queue/" + queue.value
    data = self.request(region, path)
    return LeagueListDTO.create(data)

