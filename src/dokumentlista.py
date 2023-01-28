from typing import List

from pydantic import BaseModel

from src.dokument import Dokument


class Dokumentlista(BaseModel):
    # traffar: int
    dokument: List[Dokument]
