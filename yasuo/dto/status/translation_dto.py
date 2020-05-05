from dataclasses import dataclass

@dataclass(init=True)
class TranslationDTO:
  "Translation entity"
  updated_at: str
  locale: str
  content: str

  @staticmethod
  def create(data):
    "Create TranslationDTO instance"
    return TranslationDTO(
      updated_at=data["updated_at"] if "updated_at" in data else None,
      locale=data["locale"],
      content=data["content"]
    )
