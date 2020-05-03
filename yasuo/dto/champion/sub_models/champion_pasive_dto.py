from dataclasses import dataclass
from . import ChampionImageDTO

@dataclass(init=True)
class ChampionPassiveDTO:
  name: str
  description: str
  image: ChampionImageDTO
