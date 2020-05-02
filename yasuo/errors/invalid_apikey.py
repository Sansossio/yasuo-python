class InvalidApikey(Exception):
  def __init__(self):
    super().__init__()
    self.message = "Apikey must is not valid for this method"
