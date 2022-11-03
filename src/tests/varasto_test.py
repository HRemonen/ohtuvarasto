import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.bad_varasto = Varasto(-2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_vaara_tilavuus_annettu(self):
        self.assertEqual(self.bad_varasto.tilavuus, 0.0)

    def test_vaara_saldo_annettu(self):
        self.bad_varasto = Varasto(10, -10)

        self.assertEqual(self.bad_varasto.tilavuus, 10)
        self.assertEqual(self.bad_varasto.saldo, 0)

    def test_lisaa_varastoon_alle_nolla(self):
        saldo_ennen = self.varasto.saldo

        self.varasto.lisaa_varastoon(-2)

        self.assertEqual(self.varasto.saldo, saldo_ennen)

    def test_listaa_vastoon_liikaa(self):
        saldo_ennen = self.varasto.saldo
        maks = self.varasto.paljonko_mahtuu()

        self.varasto.lisaa_varastoon(maks + 10)

        self.assertEqual(self.varasto.saldo, (saldo_ennen + maks))

    def test_ota_varastosta_alle_nolla(self):
        self.assertEqual(self.varasto.ota_varastosta(-2), 0.0)

    def test_ota_varastosta_liikaa(self):
        maks = self.varasto.saldo

        self.assertEqual(self.varasto.ota_varastosta(maks + 10), maks)

        self.assertEqual(self.varasto.saldo, 0.0)

    def test_print(self):
        assert isinstance(str(self), str)

        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
