from dataclasses import dataclass
from yasuo.dto.miniseries import MiniSeriesDTO
from . import LeagueItemDTO

@dataclass(init=True)
class LeagueEntryDTO(LeagueItemDTO):
  "League summoner entry"
  league_id: str = ""
  tier: str = ""
  queue_type: str = ""

  @staticmethod
  def create(data):
    return LeagueEntryDTO(
      league_id=data["leagueId"],
      fresh_blood=data["freshBlood"],
      wins=data["wins"],
      summoner_name=data["summonerName"],
      inactive=data["inactive"],
      veteran=data["veteran"],
      hot_streak=data["hotStreak"],
      queue_type=data["queueType"],
      tier=data["tier"],
      rank=data["rank"],
      league_points=data["leaguePoints"],
      losses=data["losses"],
      summoner_id=data["summonerId"],
      mini_series=LeagueEntryDTO._create_mini_series(data)
    )