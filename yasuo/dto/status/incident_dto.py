from dataclasses import dataclass
from typing import List
from .message_dto import MessageDTO

@dataclass(init=True)
class IncidentDTO:
  "IncidentDTO entity"
  id: str
  active: bool
  created_at: str
  updates: List[MessageDTO]

  @staticmethod
  def create(data):
    "Create IncidentDTO instance"
    updates = list(map(MessageDTO.create, data["updates"]))
    return IncidentDTO(
      id=data["id"],
      active=data["active"],
      updates=updates,
      created_at=data["created_at"]
    )
