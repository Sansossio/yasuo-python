from dataclasses import dataclass

@dataclass(init=True)
class MatchReferenceDto:
  "Match reference dto"
  game_id: int	
  role: str	
  season: int	
  platform_id: str	
  champion: int	
  queue: int	
  lane: str	
  timestamp: int

  @staticmethod
  def create(data):
    "Create MatchReferenceDto instance"
    return MatchReferenceDto(
      game_id=data["gameId"],
      role=data["role"],
      season=data["season"],
      platform_id=data["platformId"],
      champion=data["champion"],
      queue=data["queue"],
      lane=data["lane"],
      timestamp=data["timestamp"],
    )
