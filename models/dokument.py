from datetime import datetime

from pydantic import BaseModel


class Dokument(BaseModel):
    datum: str
    id: str

    @property
    def date(self):
        return datetime.strptime(self.datum, "%Y-%m-%d")
