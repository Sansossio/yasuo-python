from dataclasses import dataclass

@dataclass(init=True)
class ChampionMasteryDTO:
  "ChampionMasteryDTO - This object contains single Champion Mastery information for player and champion combination."
  # 	Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion.
  champion_points_until_next_level: int
  # 	Is chest granted for this champion or not in current season.
  chest_granted: bool
  # 	Champion ID for this entry.
  champion_id: int
  # 	Last time this champion was played by this player - in Unix milliseconds time format.
  last_play_time: int
  # 	Champion level for specified player and champion combination.
  champion_level: int
  # 	Summoner ID for this entry. (Encrypted)
  summoner_id: str
  # 	Total number of champion points for this player and champion combination - they are used to determine championLevel.
  champion_points: int
  # 	Number of points earned since current level has been achieved.
  champion_points_since_last_level: int
  # 	The token earned for this champion to levelup.
  tokens_earned: int

  @staticmethod
  def create(data):
    "Create ChampionMasteryDTO instance"
    return ChampionMasteryDTO(
      champion_points_until_next_level=data["championPointsUntilNextLevel"],
      chest_granted=data["chestGranted"],
      champion_id=data["championId"],
      last_play_time=data["lastPlayTime"],
      champion_level=data["championLevel"],
      summoner_id=data["summonerId"],
      champion_points=data["championPoints"],
      champion_points_since_last_level=data["championPointsSinceLastLevel"],
      tokens_earned=data["tokensEarned"]
    )
