from typing import List
from yasuo.apis.base_api import BaseApi
from yasuo.enum import Regions, Queues
from yasuo.dto.league import LeagueListDTO, LeagueItemDTO, LeagueEntryDTO

class LeagueApi(BaseApi):
  "Leagues api"
  __base_path = "league/v4"

  def challenger_leagues_by_queue(self, queue: Queues, region: Regions):
    "Get challenger leagues by queue"
    path = self.__base_path + "/challengerleagues/by-queue/" + queue.value
    data = self.request(region, path)
    return LeagueListDTO.create(data)

  def leagues_by_summoner_id(self, summoner_id: str, region: Regions):
    "Get summoner's leagues"
    path = self.__base_path + "/entries/by-summoner/" + summoner_id
    data = self.request(region, path)
    response: List[LeagueEntryDTO] = list(map(LeagueEntryDTO.create, data))
    return response

