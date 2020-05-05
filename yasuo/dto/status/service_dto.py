from dataclasses import dataclass
from typing import List
from .incident_dto import IncidentDTO

@dataclass(init=True)
class ServiceDTO:
  "ServiceDTO entity"
  name: str
  slug: str
  status: str
  incidents: List[IncidentDTO]

  @staticmethod
  def create(data):
    "Create ServiceDTO instance"
    incidents = list(map(IncidentDTO.create, data["incidents"]))
    return ServiceDTO(
      name=data["name"],
      slug=data["slug"],
      status=data["status"],
      incidents=incidents
    )
