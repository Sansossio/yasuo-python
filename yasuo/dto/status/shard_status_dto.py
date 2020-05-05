from dataclasses import dataclass
from typing import List
from .service_dto import ServiceDTO

@dataclass(init=True)
class ShardStatusDTO:
  "ShardStatusDTO entity"
  locales: List[str]
  hostname: str
  name: str
  services: List[ServiceDTO]
  slug: str
  region_tag: str

  @staticmethod
  def create(data):
    "Create ShardStatusDTO instance"
    services = list(map(ServiceDTO.create, data["services"]))
    return ShardStatusDTO(
      locales=data["locales"],
      hostname=data["hostname"],
      name=data["name"],
      services=services,
      slug=data["slug"],
      region_tag=data["region_tag"],
    )
