from dataclasses import dataclass
from typing import List
from .match_reference_dto import MatchReferenceDto

@dataclass(init=True)
class MatchlistDto:
  "Match list dto"
  start_index: int
  total_games: int
  end_index: int
  matches: List[MatchReferenceDto]

  @staticmethod
  def create(data):
    "Create MatchlistDto instance"
    matches = list(map(MatchReferenceDto.create, data["matches"]))
    return MatchlistDto(
      start_index=data["startIndex"],
      total_games=data["totalGames"],
      end_index=data["endIndex"],
      matches=matches
    )
