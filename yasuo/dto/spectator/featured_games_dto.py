from dataclasses import dataclass
from typing import List
from .featured_game_info_dto import FeaturedGameInfoDTO

@dataclass(init=True)
class FeaturedGamesDTO:
  "FeaturedGames DTO"
  # The suggested interval to wait before requesting FeaturedGames again
  client_refresh_interval: int
  # The list of featured games
  game_list: List[FeaturedGameInfoDTO]

  @staticmethod
  def create(data):
    "Create FeaturedGamesDTO instance"
    game_list = list(map(FeaturedGameInfoDTO.create, data["gameList"]))
    return FeaturedGamesDTO(
      client_refresh_interval=data["clientRefreshInterval"],
      game_list=game_list
    )
