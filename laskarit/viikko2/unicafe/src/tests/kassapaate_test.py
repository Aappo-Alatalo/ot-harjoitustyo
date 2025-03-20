import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()
  
  def test_kassapaate_on_luotu_oikein(self):
    self.assertNotEqual(self.kassapaate, None)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(self.kassapaate.edulliset, 0)
    self.assertEqual(self.kassapaate.maukkaat, 0)

  def test_kateisosto_toimii_edullinen(self):
    vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(vaihtoraha, 0)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_kateisosto_ei_hyvaksy_liian_vahan_rahaa_edullinen(self):
    vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(230)
    self.assertEqual(vaihtoraha, 230)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_kateisosto_toimii_maukas(self):
    vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(vaihtoraha, 0)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    self.assertEqual(self.kassapaate.maukkaat, 1)

  def test_kateisosto_ei_hyvaksy_liian_vahan_rahaa_maukas(self):
    vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(390)
    self.assertEqual(vaihtoraha, 390)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(self.kassapaate.maukkaat, 0)

  def test_korttiosto_toimii_edullinen(self):
    kortti = Maksukortti(240)
    tulos = self.kassapaate.syo_edullisesti_kortilla(kortti)
    self.assertEqual(tulos, True)
    self.assertEqual(kortti.saldo, 0)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) # Kassan rahamäärä ei muutu!
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_korttiosto_ei_hyvaksy_liian_vahan_rahaa_edullinen(self):
    kortti = Maksukortti(230)
    tulos = self.kassapaate.syo_edullisesti_kortilla(kortti)
    self.assertEqual(tulos, False)
    self.assertEqual(kortti.saldo, 230)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_korttiosto_toimii_maukas(self):
    kortti = Maksukortti(400)
    tulos = self.kassapaate.syo_maukkaasti_kortilla(kortti)
    self.assertEqual(tulos, True)
    self.assertEqual(kortti.saldo, 0)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(self.kassapaate.maukkaat, 1)

  def test_korttiosto_ei_hyvaksy_liian_vahan_rahaa_maukas(self):
    kortti = Maksukortti(390)
    tulos = self.kassapaate.syo_maukkaasti_kortilla(kortti)
    self.assertEqual(tulos, False)
    self.assertEqual(kortti.saldo, 390)
    self.assertEqual(self.kassapaate.maukkaat, 0)

  def test_lataa_rahaa_kortille_toimii(self):
    kortti = Maksukortti(0)
    self.kassapaate.lataa_rahaa_kortille(kortti, 100)
    self.assertEqual(kortti.saldo, 100)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

  # Exercise 9
  def test_lataa_rahaa_kortille_ei_toimi_kun_ladattava_summa_negatiivinen(self):
    kortti = Maksukortti(0)
    self.kassapaate.lataa_rahaa_kortille(kortti, -100)
    self.assertEqual(kortti.saldo, 0)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  def test_kassassa_rahaa_euroina_toimii_oikein(self):
    self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)