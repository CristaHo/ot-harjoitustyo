import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_lataus_onnistuu(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
    
    def test_ota_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
    
    def test_ota_liikaa_rahaa(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_ota_rahaa_true(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ota_liikaa_rahaa_false(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
    
    