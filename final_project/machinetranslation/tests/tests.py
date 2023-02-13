
import unittest
from translator import english_to_french
from translator import french_to_english
entext1 = " "
frtext1 = " "
entext2 = "Hello"
frtext2 = "Bonjour"

class TestTranslator(unittest.TestCase):

    def test_enfr_null(self):
        self.assertEqual(frtext1,english_to_french(entext1))

    def test_fren_null(self):
        self.assertEqual(entext1,french_to_english(frtext1))

    def test_enfr_hello(self):
        self.assertEqual(frtext2,english_to_french(entext2))

    def test_fren_hello(self):
        self.assertEqual(entext2,french_to_english(frtext2))

if __name__ == '__main__':
    unittest.main()