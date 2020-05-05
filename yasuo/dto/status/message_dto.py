from dataclasses import dataclass
from typing import List
from .translation_dto import TranslationDTO

@dataclass(init=True)
class MessageDTO:
  "MessageDTO entity"
  message_id: str
  severity: str
  content: str
  author: str
  translations: List[TranslationDTO]
  updated_at: str
  created_at: str

  @staticmethod
  def create(data):
    "Create MessageDTO instance"
    translations = list(map(TranslationDTO.create, data["translations"]))
    return MessageDTO(
      message_id=data["id"],
      severity=data["severity"],
      content=data["content"],
      author=data["author"],
      translations=translations,
      updated_at=data["updated_at"],
      created_at=data["created_at"]
    )
