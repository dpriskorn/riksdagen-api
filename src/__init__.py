import requests
from pydantic import BaseModel

from src.dokumentlista import Dokumentlista
from src.exceptions import DocumentNotFound


class Riksdagen(BaseModel):

    @staticmethod
    def lookup_document_html_by_id(id: str):
        base_url = "https://data.riksdagen.se/dokument/"
        response = requests.get(base_url + id, params=None)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            raise DocumentNotFound("No document with this ID found at Riksdagen")
        else:
            raise ValueError(f"Got {response.status_code} from Riksdagen, {response.text}")

    @staticmethod
    def lookup_document_metadata_by_id(id: str):
        base_url = (f"https://data.riksdagen.se/dokumentlista/?sok={id}"
                    f"&doktyp=&rm=&from=&tom=&ts=&bet=&tempbet=&nr=&org="
                    f"&iid=&avd=&webbtv=&talare=&exakt=&planering=&facets="
                    f"&sort=rel&sortorder=desc&rapport=&utformat=json&a=s#soktraff")
        params = {
            "Accept": "application/json"
        }
        response = requests.get(base_url + id, params=params)
        if response.status_code == 200:
            json_data = response.json()
            # print(json_data)
            # print(json_data["dokumentlista"])
            lista = Dokumentlista(**json_data["dokumentlista"])
            return lista
            # raise DocumentNotFound("No document with this ID found at Riksdagen")
        else:
            raise ValueError(f"Got {response.status_code} from Riksdagen, {response.text}")
