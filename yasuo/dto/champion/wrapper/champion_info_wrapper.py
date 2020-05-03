from ..sub_models import *

def wrapper_champion_skin(data):
  return ChampionSkinDTO(
    id=data["id"],
    num=data["num"],
    name=data["name"],
    chromas=data["chromas"]
  )

def wrapper_champion_image(data):
  return ChampionImageDTO(
      full=data["full"],
      sprite=data["sprite"],
      group=data["group"],
      x=data["x"],
      y=data["y"],
      w=data["w"],
      h=data["h"]
    )

def wrapper_champion_info(data):
  return ChampionInfoDTO(
    attack=data["attack"],
    defense=data["defense"],
    magic=data["magic"],
    difficulty=data["difficulty"]
  )

def wrapper_champion_stats(data):
  return ChampionStatsDTO(
    hp=data["hp"],
    hpperlevel=data["hpperlevel"],
    mp=data["mp"],
    mpperlevel=data["mpperlevel"],
    movespeed=data["movespeed"],
    armor=data["armor"],
    armorperlevel=data["armorperlevel"],
    spellblock=data["spellblock"],
    spellblockperlevel=data["spellblockperlevel"],
    attackrange=data["attackrange"],
    hpregen=data["hpregen"],
    hpregenperlevel=data["hpregenperlevel"],
    mpregen=data["mpregen"],
    mpregenperlevel=data["mpregenperlevel"],
    crit=data["crit"],
    critperlevel=data["critperlevel"],
    attackdamage=data["attackdamage"],
    attackdamageperlevel=data["attackdamageperlevel"],
    attackspeedperlevel=data["attackspeedperlevel"],
    attackspeed=data["attackspeed"]
  )

def wrapper_champion_spell(data):
  return ChampionSpellDTO(
    id=data["id"],
    name=data["name"],
    description=data["description"],
    tooltip=data["tooltip"],
    maxrank=data["maxrank"],
    cooldown=data["cooldown"],
    cooldownBurn=data["cooldownBurn"],
    cost=data["cost"],
    costBurn=data["costBurn"],
    effectBurn=data["effectBurn"],
    costType=data["costType"],
    maxammo=data["maxammo"],
    range=data["range"],
    rangeBurn=data["rangeBurn"],
    image=data["image"],
    resource=data["resource"]
  )

def wrapper_champion_passive(data):
  return ChampionPassiveDTO(
    name=data["name"],
    description=data["description"],
    image=wrapper_champion_image(data["image"])
  )