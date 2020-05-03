from dataclasses import dataclass

@dataclass(init=True)
class ChampionStatsDTO:
  hp: int
  hpperlevel: int
  mp: int
  mpperlevel: int
  movespeed: int
  armor: int
  armorperlevel: int
  spellblock: int
  spellblockperlevel: int
  attackrange: int
  hpregen: int
  hpregenperlevel: int
  mpregen: int
  mpregenperlevel: int
  crit: int
  critperlevel: int
  attackdamage: int
  attackdamageperlevel: int
  attackspeedperlevel: int
  attackspeed: int
