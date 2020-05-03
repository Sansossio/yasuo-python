from dataclasses import dataclass

@dataclass(init=True)
class ChampionImageDTO:
  "Champion image information"
  full: str
  sprite: str
  group: str
  x: int
  y: int
  w: int
  h: int
