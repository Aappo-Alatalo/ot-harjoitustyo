import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_saldon_kasvatus_toimii(self):
        self.maksukortti.lataa_rahaa(240)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12.4)

    def test_saldon_vahennys_toimii(self):
        self.maksukortti.ota_rahaa(240)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_saldon_vahennys_ei_toimi_jos_ei_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_jos_rahat_riittivat(self):
        tulos = self.maksukortti.ota_rahaa(500)
        self.assertEqual(tulos, True)
    
    def test_ota_rahaa_palauttaa_false_jos_rahat_eivat_riita(self):
        tulos = self.maksukortti.ota_rahaa(1100)
        self.assertEqual(tulos, False)