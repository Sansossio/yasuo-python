from dataclasses import dataclass

@dataclass(init=True)
class ParticipantDTO:
  "Participant details"
  # Flag indicating whether or not this participant is a bot
  bot: bool
  # The ID of the second summoner spell used by this participant
  spell2_id: int
  # The ID of the profile icon used by this participant
  profile_icon_id: int
  # The summoner name of this participant
  summoner_name: str
  # The ID of the champion played by this participant
  champion_id: int
  # The team ID of this participant, indicating the participant's team
  team_id: int
  # The ID of the first summoner spell used by this participant
  spell1_id: int

  @staticmethod
  def create(data):
    return ParticipantDTO(
      bot=data["bot"],
      spell2_id=data["spell2Id"],
      profile_icon_id=data["profileIconId"],
      summoner_name=data["summonerName"],
      champion_id=data["championId"],
      team_id=data["teamId"],
      spell1_id=data["spell1Id"]
    )
