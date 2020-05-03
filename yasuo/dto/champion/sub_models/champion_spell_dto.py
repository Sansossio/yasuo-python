from dataclasses import dataclass
from typing import List
from .champion_image_dto import ChampionImageDTO

@dataclass(init=True)
class ChampionSpellDTO:
  id: str
  name: str
  description: str
  tooltip: str
  maxrank: int
  cooldown: List[int]
  cooldownBurn: str
  cost: List[int]
  costBurn: str
  effectBurn: List[int]
  costType: str
  maxammo: str
  range: int
  rangeBurn: str
  image: ChampionImageDTO
  resource: str
