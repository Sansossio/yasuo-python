from dataclasses import dataclass
from typing import List
from .sub_models import *
from .wrapper import *

@dataclass(init=True)
class ChampionDTO:
  "Champion details"
  champion_id: str
  key: str
  name: str
  title: str
  image: ChampionImageDTO
  skins: List[ChampionSkinDTO]
  lore: str
  blurb: str
  allytips: List[str]
  enemytips: List[str]
  tags: List[str]
  partype: str
  info: ChampionInfoDTO
  stats: ChampionStatsDTO
  spells: ChampionSpellDTO
  passive: ChampionPassiveDTO
  allytips: List[str]
  enemytips: List[str]

  @staticmethod
  def __mapSkins (data):
    return ChampionSkinDTO(
      id=data["id"],
      num=data["num"],
      name=data["name"],
      chromas=data["chromas"]
    )

  @staticmethod
  def create (data):
    "Create ChampionInfo instance"
    champion_name = list(data["data"].keys())[0]
    champion_info = data["data"][champion_name]
    return ChampionDTO(
      champion_id=champion_info["id"],
      key=champion_info["key"],
      name=champion_info["name"],
      title=champion_info["title"],
      image=wrapper_champion_image(champion_info["image"]),
      skins=map(wrapper_champion_skin, champion_info["skins"]),
      lore=champion_info["lore"],
      blurb=champion_info["blurb"],
      allytips=champion_info["allytips"],
      enemytips=champion_info["enemytips"],
      tags=champion_info["tags"],
      partype=champion_info["partype"],
      info=wrapper_champion_info(champion_info["info"]),
      stats=wrapper_champion_stats(champion_info["stats"]),
      spells=map(wrapper_champion_spell, champion_info["spells"]),
      passive=wrapper_champion_passive(champion_info["passive"])
    )
