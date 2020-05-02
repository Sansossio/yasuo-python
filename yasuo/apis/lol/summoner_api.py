from yasuo.apis.base_api import BaseApi
from yasuo.enum.regions import Regions

# Summoner api
class SummonerApi(BaseApi):
  def getByName (self, summoner_name: str, region: Regions):
    return region
