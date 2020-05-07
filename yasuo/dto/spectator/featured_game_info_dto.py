from dataclasses import dataclass
from typing import List
from .observer_dto import ObserverDTO
from .banned_champion_dto import BannedChampionDTO
from .participant_dto import ParticipantDTO

@dataclass(init=True)
class FeaturedGameInfoDTO:
  "Game information"
  # The game mode (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
  game_mode: str
  # The amount of time in seconds that has passed since the game started
  game_length: int
  # The ID of the map
  map_id: int
  # The game type (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
  game_type: str
  # Banned champion information
  banned_champions: List[BannedChampionDTO]
  # The ID of the game
  game_id: int
  # The observer information
  observers: ObserverDTO
  # The queue type (queue types are documented on the Game Constants page)
  game_queue_config_id: int
  # The game start time represented in epoch milliseconds
  game_start_time: int
  # The participant information
  participants: List[ParticipantDTO]
  # The ID of the platform on which the game is being played
  platform_id: str

  @staticmethod
  def create(data):
    "Create Featured Game Info Instance"
    banned_champions = list(map(BannedChampionDTO.create, data["bannedChampions"]))
    participants = list(map(ParticipantDTO.create, data["participants"]))
    return FeaturedGameInfoDTO(
      game_mode=data["gameMode"],
      game_length=data["gameLength"],
      map_id=data["mapId"],
      game_type=data["gameType"],
      banned_champions=banned_champions,
      game_id=data["gameId"],
      observers=ObserverDTO.create(data["observers"]),
      game_queue_config_id=data["gameQueueConfigId"],
      game_start_time=data["gameStartTime"],
      participants=participants,
      platform_id=data["platformId"]
    )