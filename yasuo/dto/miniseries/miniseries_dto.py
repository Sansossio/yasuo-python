from dataclasses import dataclass

@dataclass(init=True)
class MiniSeriesDTO:
  "Miniseries DTO"
  losses: int
  progress: int
  target: int
  wins: int

  @staticmethod
  def create(data):
    return MiniSeriesDTO(
      losses=data["losses"],
      progress=data["progress"],
      target=data["target"],
      wins=data["wins"]
    )
