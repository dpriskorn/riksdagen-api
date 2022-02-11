import requests
from pydantic import BaseModel

from models.exceptions import DocumentNotFound


class Riksdagen(BaseModel):

    def lookup_id(self, id: str):
        base_url = "https://data.riksdagen.se/dokument/"
        response = requests.get(base_url + id)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            raise DocumentNotFound("No document with this ID found at Riksdagen")
        else:
            raise ValueError(f"Got {response.status_code} from Riksdagen, {response.text}")