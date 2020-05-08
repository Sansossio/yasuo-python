from dataclasses import dataclass

@dataclass(init=True)
class BannedChampionDTO:
  "BannedChampion DTO"
  # The turn during which the champion was banned
  pick_turn: int
  # The ID of the banned champion
  champion_id: int
  # The ID of the team that banned the champion
  team_id: int

  @staticmethod
  def create(data):
    return BannedChampionDTO(
      pick_turn=data["pickTurn"],
      champion_id=data["championId"],
      team_id=data["teamId"]
    )
