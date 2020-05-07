from dataclasses import dataclass

@dataclass(init=True)
class BannedChampionDTO:
  "BannedChampion"
  # The turn during which the champion was banned
  pick_turn: int
  # The ID of the banned champion
  champion_id: int
  # The ID of the team that banned the champion
  team_id: int

  @staticmethod
  def create(data):
    return BannedChampionDTO(
      pick_turn=data["pick_turn"],
      champion_id=data["champion_id"],
      team_id=data["team_id"]
    )
