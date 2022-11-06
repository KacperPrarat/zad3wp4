import  unittest

from drugiprogram import  drugafunkcja

class Test_program(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(drugafunkcja(2,3),5)
c