import unittest
from app import Supperhero


class TestSupperhero(unittest.TestCase):

    def setUp(self):
        self.hero1 = Supperhero("Hero1", 10)
        self.hero2 = Supperhero("Hero2", 5)
        self.hero3 = Supperhero("Hero3", 10)

    def test_stronger_hero(self):
        self.assertTrue(self.hero1.is_stronger_than(self.hero2))

    def test_weaker_hero(self):
        self.assertFalse(self.hero2.is_stronger_than(self.hero1))

    def test_equal_strength(self):
        self.assertFalse(self.hero1.is_stronger_than(self.hero3))
        self.assertFalse(self.hero3.is_stronger_than(self.hero1))

    def test_str_method(self):
        self.assertEqual(str(self.hero1), "Hero1")


if __name__ == "__main__":
    unittest.main()
