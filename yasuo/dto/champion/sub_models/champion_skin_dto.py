from dataclasses import dataclass

@dataclass(init=True)
class ChampionSkinDTO:
  "Champion skin information"
  id: str
  num: int
  name: str
  chromas: bool
