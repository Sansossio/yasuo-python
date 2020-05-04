from dataclasses import dataclass
from . import LeagueItemDTO
from typing import List

@dataclass(init=True)
class LeagueListDTO:
  "League list"
  league_id: str
  entries: List[LeagueItemDTO]
  tier: str
  name: str
  queue: str

  @staticmethod
  def create(data):
    entries = list(map(LeagueItemDTO.create, data["entries"]))
    return LeagueListDTO(
      league_id=data["leagueId"],
      entries=entries,
      tier=data["tier"],
      name=data["name"],
      queue=data["queue"]
    )
