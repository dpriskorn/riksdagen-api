from datetime import datetime

from pydantic import BaseModel


class Dokument(BaseModel):
    """This models a document in Riksdagen"""
    datum: str
    id: str

    @property
    def date(self):
        return datetime.strptime(self.datum, "%Y-%m-%d")
