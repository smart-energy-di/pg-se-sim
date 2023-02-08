import unittest

from model.simobject import SeObject


class SimObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.seObject = SeObject()

    def test_01(self):
        self.assertEqual(type(self.seObject), SeObject)
        self.assertEqual(str(type(self.seObject)),
                         "<class 'model.simobject.SeObject'>")


if __name__ == '__main__':
    unittest.main()
