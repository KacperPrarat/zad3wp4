import unittest

from program import funkcja

class Test_program(unittest.TestCase):

    def test_mnozenie(self):

        self.assertEqual(funkcja(2),4)
