from dataclasses import dataclass

@dataclass(init=True)
class ChampionInfoDTO:
  attack: int
  defense: int
  magic: int
  difficulty: int
