from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions
from yasuo.dto.status import ShardStatusDTO

class StatusApi(BaseApi):
  "Status api"
  __base_path = "status/v3/shard-data"

  def shard_status(self, region: Regions):
    "Get League of Legends status for the given shard."
    response = self.request(region, self.__base_path)
    return ShardStatusDTO.create(response)
