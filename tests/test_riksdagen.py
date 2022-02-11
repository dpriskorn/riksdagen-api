from unittest import TestCase

from models.exceptions import DocumentNotFound
from models.riksdagen import Riksdagen


class TestRiksdagen(TestCase):
    def test_lookup_id(self):
        rd = Riksdagen()
        if not rd.lookup_id("GZ01MJU21"):
            self.fail()

    def test_lookup_id_with_invalid_id(self):
        rd = Riksdagen()
        # https://www.geeksforgeeks.org/unit-testing-python-unittest/
        with self.assertRaises(DocumentNotFound):
            rd.lookup_id("GZ01MJU21XX")

