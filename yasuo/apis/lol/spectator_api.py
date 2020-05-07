from typing import List
from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.spectator import FeaturedGamesDTO

class SpectatorApi(BaseApi):
  "Spectator"
  __base_path = "spectator/v4"
  
  def featured_games(self, region: Regions):
    "Get list of featured games."
    path = self.__base_path + "/featured-games"
    data = self.request(region, path)
    return FeaturedGamesDTO.create(data)
