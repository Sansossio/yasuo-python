class ApikeyNotFound(Exception):
  def __init__(self):
    super().__init__()
    self.message = "Apikey must be defiend"
