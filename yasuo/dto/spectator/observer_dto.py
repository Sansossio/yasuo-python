from dataclasses import dataclass

@dataclass(init=True)
class ObserverDTO:
  "Observer DTO"
  # Key used to decrypt the spectator grid game data for playback
  encryption_key: str

  @staticmethod
  def create(data):
    return ObserverDTO(
      encryption_key=data["encryptionKey"]
    )
