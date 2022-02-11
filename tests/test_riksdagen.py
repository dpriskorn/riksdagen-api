from datetime import datetime
from unittest import TestCase

from src.models.dokumentlista import Dokumentlista
from src.models.exceptions import DocumentNotFound
from src.models.riksdagen import Riksdagen


class TestRiksdagen(TestCase):
    def test_lookup_id(self):
        rd = Riksdagen()
        if not rd.lookup_document_html_by_id("GZ01MJU21"):
            self.fail()

    def test_lookup_id_with_invalid_id(self):
        rd = Riksdagen()
        # https://www.geeksforgeeks.org/unit-testing-python-unittest/
        with self.assertRaises(DocumentNotFound):
            rd.lookup_document_html_by_id("GZ01MJU21XX")

    # def test_lookup_id_response(self):
    #     rd = Riksdagen()
    #     print(rd.lookup_document_html_by_id("GZ01MJU21"))

    # def test_lookup_document_metadata_by_id(self):
    #     rd = Riksdagen()
    #     if not rd.lookup_document_metadata_by_id("GZ01MJU21"):
    #         self.fail()

    # def test_lookup_document_metadata_by_id_with_invalid_id(self):
    #     rd = Riksdagen()
    #     # https://www.geeksforgeeks.org/unit-testing-python-unittest/
    #     with self.assertRaises(DocumentNotFound):
    #         rd.lookup_document_metadata_by_id("GZ01MJU21XX")

    def test_lookup_document_metadata_by_id_response(self):
        rd = Riksdagen()
        dokumentlista = rd.lookup_document_metadata_by_id("GZ01MJU21")
        # print(dokumentlista)
        if not dokumentlista:
            self.fail()
        if not isinstance(dokumentlista, Dokumentlista):
            self.fail()
        if not len(dokumentlista.dokument) == 1:
            self.fail()
        if dokumentlista.dokument[0].date != datetime(year=2012, month=6, day=4):
            self.fail()
