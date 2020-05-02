from dataclasses import dataclass
from typing import List

@dataclass(init=True)
class ChampionInfoDTO:
  "Champion rotation info"
  max_new_player_level: int
  free_champion_ids_for_new_players: List[int]
  free_champion_ids: List[int]

  @staticmethod
  def create (data):
    "Create ChampionInfo instance"
    return ChampionInfoDTO(
      max_new_player_level=data["maxNewPlayerLevel"],
      free_champion_ids_for_new_players=data["freeChampionIdsForNewPlayers"],
      free_champion_ids=data["freeChampionIds"]
    )
