from typing import List
from yasuo.apis.base_api import BaseApi
from yasuo.enum import Regions, Queues
from yasuo.dto.league import LeagueListDTO

class LeagueApi(BaseApi):
  "Leagues api"
  __base_path = "league/v4"

  def challenger_leagues_by_queue(self, queue: Queues, region: Regions):
    "Get challenger leagues by queue"
    path = self.__base_path + "/challengerleagues/by-queue/" + queue.value
    response = self.request(region, path)
    return LeagueListDTO.create(response)
