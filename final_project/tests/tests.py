import unittest
from machinetranslation.translator import english_to_french,french_to_english

class TranslatorTest(unittest.TestCase):
    def test_english2French(self):
        return self.assertEqual(english_to_french("Hello"),"Bonjour")
    
    def test_french2English(self):
        return self.assertEqual(french_to_english("Bonjour"),"Hello")
    
    def test_en2fr(self):
        return self.assertNotEqual(english_to_french("Hai"),"Bonjour")
    
    def test_fr2en(self):
        return self.assertNotEqual(french_to_english("Bonjour"),"Hai")
    
if __name__ == '__main__':
    unittest.main()