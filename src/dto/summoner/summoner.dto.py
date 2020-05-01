from dataclasses import dataclass

@dataclass(init=True)
# SummonerDTO - represents a summoner
class SummonerDTO:
  # Encrypted account ID. Max length 56 characters.
  account_id: str
  # ID of the summoner icon associated with the summoner.
  profile_icon_id: int
  # Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
  revision_date: int
  # Summoner name.
  name: str
  # Encrypted summoner ID. Max length 63 characters.
  id: str
  # Encrypted PUUID. Exact length of 78 characters.
  puuid: str
  # Summoner level associated with the summoner.
  summoner_level: int
