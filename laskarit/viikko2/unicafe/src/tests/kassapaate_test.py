import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassassa_rahaa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_ostetut_lounaat(self):
        self.assertEqual((self.kassa.edulliset + self.kassa.maukkaat), 0)
    
    def test_maukas_lounas_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
    
    def test_maukas_lounas_kateisella_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200), 200)
    
    def test_maukas_lounas_kateisella_kassan_rahat(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_maukas_lounas_kateisella_vahan_rahaa_kassan_rahat(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maukas_lounas_kateisella_maara(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukas_lounas_kateisella_vahan_rahaa_maara(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_maukas_lounas_kortilla(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
    
    def test_maukas_lounas_kortilla_kortilta_rahat(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)
    
    def test_maukas_lounas_kortilla_maara(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukas_lounas_kortilla_kassan_maara(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maukas_lounas_kortilla_ei_rahaa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
    
    def test_maukas_lounas_kortilla_ei_rahaa_maara(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_maukas_lounas_kortilla_ei_rahaa_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
    
    def test_edullinen_lounas_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)
    
    def test_edullinen_lounas_kateisella_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)
    
    def test_edullinen_lounas_kateisella_kassan_rahat(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_edullinen_lounas_kateisella_vahan_rahaa_kassan_rahat(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edullinen_lounas_kateisella_maara(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullinen_lounas_kateisella_vahan_rahaa_maara(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_edullinen_lounas_kortilla(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
    
    def test_edullinen_lounas_kortilla_kortilta_rahat(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)
    
    def test_edullinen_lounas_kortilla_maara(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullinen_lounas_kortilla_kassan_maara(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edullinen_lounas_kortilla_ei_rahaa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
    
    def test_edullinen_lounas_kortilla_ei_rahaa_maara(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_edullinen_lounas_kortilla_ei_rahaa_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
    
    def test_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)
    
    def test_lataa_rahaa_kortille_kassa_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)
    
    def test_lataa_rahaa_miinus(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, 1000)