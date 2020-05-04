from dataclasses import dataclass
from yasuo.dto.miniseries import MiniSeriesDTO

@dataclass(init=True)
class LeagueItemDTO:
  "League item"
  fresh_blood: bool
  wins: int
  summoner_name: str
  inactive: bool
  veteran: bool
  hot_streak: bool
  rank: str
  league_points: int
  losses: int
  summoner_id: str
  mini_series: MiniSeriesDTO

  @staticmethod
  def create(data):
    mini_series = MiniSeriesDTO.create(data["miniSeries"]) if "miniSeries" in data else []
    return LeagueItemDTO(
      fresh_blood=data["freshBlood"],
      wins=data["wins"],
      summoner_name=data["summonerName"],
      inactive=data["inactive"],
      veteran=data["veteran"],
      hot_streak=data["hotStreak"],
      rank=data["rank"],
      league_points=data["leaguePoints"],
      losses=data["losses"],
      summoner_id=data["summonerId"],
      mini_series=mini_series
    )