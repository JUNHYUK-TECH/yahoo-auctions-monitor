import unittest
from yahoo_monitor import allowed, parse_price, accessory_only

class MonitorFilterTests(unittest.TestCase):
    def test_price_bounds(self):
        self.assertFalse(allowed("PRS", "PRS Custom 24", 100000))
        self.assertTrue(allowed("PRS", "PRS Custom 24", 100001))
        self.assertFalse(allowed("PRS", "PRS Custom 24", 1000000))
    def test_gibson(self):
        self.assertTrue(allowed("Gibson", "Gibson ES-335 2014", 300000))
        self.assertFalse(allowed("Gibson", "Epiphone by Gibson Les Paul", 300000))
    def test_fender(self):
        self.assertTrue(allowed("Fender", "Fender Custom Shop Stratocaster", 200000))
        self.assertFalse(allowed("Fender", "Fender Made in Japan Traditional", 200000))
        self.assertTrue(allowed("Fender", "Fender 新井和輝 signature made in Japan", 200000))
    def test_current_price(self):
        self.assertEqual(parse_price("現在価格 123,456円 即決 200,000円"), 123456)
    def test_accessory_filter(self):
        self.assertTrue(accessory_only("Fender official case"))
        self.assertFalse(accessory_only("Fender Custom Stratocaster with hard case"))

if __name__ == "__main__":
    unittest.main()
