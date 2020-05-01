import dataclasses

@dataclasses
# SummonerDTO - represents a summoner
class SummonerDTO:
  # Encrypted account ID. Max length 56 characters.
  accountId: str
  # ID of the summoner icon associated with the summoner.
  profileIconId: int
  # Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
  revisionDate: int
  # Summoner name.
  name: str
  # Encrypted summoner ID. Max length 63 characters.
  id: str
  # Encrypted PUUID. Exact length of 78 characters.
  puuid: str
  # Summoner level associated with the summoner.
  summonerLevel: int
